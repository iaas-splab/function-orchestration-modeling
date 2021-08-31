import ibm_boto3
import ibm_botocore
from ibm_boto3.s3.transfer import TransferConfig
from ibm_botocore.client import Config
from ibm_botocore import UNSIGNED

import os
import logging
import gzip
import json
import pandas as pd
from pandas.io.json import json_normalize

OPENAQ_BUCKET = 'openaq-fetches'
COS_OUTPUT_BUCKET = 'openaq-output'
TEMP_FOLDER_TEMPLATE = 'openaq/temp/{}'

# IBM Cloud Functions default environment variables
# For more info: https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-actions#actions_envvars
IAM_API_KEY = os.environ.get('__OW_IAM_NAMESPACE_API_KEY')
ACTIVATION_ID = os.environ.get('__OW_ACTIVATION_ID')
ENDPOINT = 'https://s3.private.eu-de.cloud-object-storage.appdomain.cloud'

s3 = ibm_boto3.client('s3', config=Config(signature_version=UNSIGNED))
ibm_cos = ibm_boto3.client("s3",
    ibm_api_key_id=IAM_API_KEY,
    config=Config(signature_version="oauth"),
    endpoint_url=ENDPOINT
)

log = logging.getLogger()


def download_data(filename):
    """Download a file from IBM Cloud Object Storage
    Parameters
    ----------
    filename: string, required
        Name of the file in IBM Cloud Object Storage source bucket (OpenAQ)
    Returns
    -------
    data_file: string
        Local path to downloaded file
    """
    
    try:
        config = TransferConfig(max_concurrency=2)
        data_file = os.path.join('/tmp', os.path.basename(filename))
        s3.download_file(OPENAQ_BUCKET, filename, data_file, Config=config)
    except ibm_botocore.exceptions.ClientError as e:
        log.error(f'Unable to download data: {filename}')
        log.debug(e)
        raise
    return data_file

def process_data(dataframes):
    """Combine datasets and process to extract required fields
    Parameters
    ----------
    dataframes: list of Pandas dataframes, required
        List of dataframes with raw air quality data
    Returns
    -------
    parameter_readings: Pandas dataframe
        Processed dataframe of air quality ratings
    """
    
    try:
        # combine into single dataframe
        data = pd.concat(dataframes, sort=False)
        
        # keep only coulumns we need
        columns_to_keep = ['country','city','location','parameter','value', 'unit','date.utc']
        data.drop(set(data.columns.values) - set(columns_to_keep), axis=1, inplace=True)
        log.info(f"Total rows to process: {len(data)}")

        # pivot to convert air quality parameters to columns
        parameter_readings = data.pivot_table(
            index=[
                'country',
                'city',
                'location',
                'date.utc'],
            columns='parameter',
            values='value').reset_index()
    except Exception as e:
        log.error("Error processing data")
        log.debug(e)

    return parameter_readings


def upload_intermediate_results(results):
    """Upload a file to IBM Cloud Object Storage
    Parameters
    ----------
    results: string, required
        Name of the local file with intermediate results
    """
    
    results_path = os.path.join('/tmp', results)
    try:
        response = ibm_cos.upload_file(
            results_path,
            COS_OUTPUT_BUCKET,
            TEMP_FOLDER_TEMPLATE.format(results))
        log.info("Uploaded intermediate results to bucket {}, path: ".format(COS_OUTPUT_BUCKET) + TEMP_FOLDER_TEMPLATE.format(results))
    except ibm_botocore.exceptions.ClientError as e:
        log.error(f'Unable to upload intermediate results: {results}')
        log.debug(e)
        raise

def main(event):
    dataframes = []
    
    # download files locally
    for filename in event['value']:
        log.info(f"downloading the following file: {filename}")
        data_file = download_data(filename)
        # read each file and store as Pandas dataframe
        with gzip.open(data_file, 'rb') as ndjson_file:
            records = map(json.loads,ndjson_file)
            df = pd.DataFrame.from_records(json_normalize(records))
            dataframes.append(df)

    # process the data to get air quality readings
    parameter_readings = process_data(dataframes)

    # write to file
    results_filename = "{}.json.gz".format(ACTIVATION_ID)
    parameter_readings.to_json(
        os.path.join(
            '/tmp',
            results_filename),
        compression='gzip')

    # upload to target IBM Cloud Object Storage bucket
    upload_intermediate_results(results_filename)

    # return temp file and number of rows processed.
    return {
        "message": "Mapper phase complete.",
        "processed_file": results_filename,
        "rows": len(parameter_readings)}