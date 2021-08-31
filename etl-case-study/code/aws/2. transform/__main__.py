import boto3
from boto3.s3.transfer import TransferConfig
import botocore
import gzip
import json
import logging
import os
import pandas as pd
import warnings

from pandas.io.json import json_normalize

s3 = boto3.client('s3')

OPENAQ_BUCKET = 'openaq-fetches'
RESULTS_BUCKET = os.environ['RESULTS_BUCKET']
TEMP_FOLDER_TEMPLATE = 'openaq/temp/{}'

log = logging.getLogger()


def download_data(filename):
    """Download a file from S3
    Parameters
    ----------
    filename: string, required
        Name of the file in S3 source bucket (OpenAQ)
    Returns
    -------
    data_file: string
        Local path to downloaded file
    """

    try:
        config = TransferConfig(max_concurrency=2)
        data_file = os.path.join('/tmp', os.path.basename(filename))
        s3.download_file(OPENAQ_BUCKET, filename, data_file, Config=config)
    except botocore.exceptions.ClientError as e:
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
    """Upload a file to S3
    Parameters
    ----------
    results: string, required
        Name of the local file with intermediate results
    """

    results_path = os.path.join('/tmp', results)
    # upload to target S3 bucket
    try:
        response = s3.upload_file(
            results_path,
            RESULTS_BUCKET,
            TEMP_FOLDER_TEMPLATE.format(results))
        log.info("Uploaded temp results to s3://{}/".format(RESULTS_BUCKET) + TEMP_FOLDER_TEMPLATE.format(results))
    except botocore.exceptions.ClientError as e:
        log.error(f'Unable to upload intermediate results: {results}')
        log.debug(e)
        raise

def main(event, context):
    dataframes = []
    # download files locally
    for filename in event:
        data_file = download_data(filename)
        # read each file and store as Pandas dataframe
        with gzip.open(data_file, 'rb') as ndjson_file:
            records = map(json.loads,ndjson_file)
            df = pd.DataFrame.from_records(json_normalize(records))
            dataframes.append(df)

    # process the data to get air quality readings
    parameter_readings = process_data(dataframes)

    # write to file
    results_filename = "{}.json.gz".format(context.aws_request_id)
    parameter_readings.to_json(
        os.path.join(
            '/tmp',
            results_filename),
        compression='gzip')

    # upload to target S3 bucket
    upload_intermediate_results(results_filename)

    # return temp file and number of rows processed.
    return {
        "message": "Mapper phase complete",
        "processed_file": results_filename,
        "rows": len(parameter_readings)}