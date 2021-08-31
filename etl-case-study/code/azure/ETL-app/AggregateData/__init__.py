from azure.storage.blob import BlobClient

import os
import tempfile
import logging
import gzip
import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
from datetime import datetime, timedelta

connection_str = os.environ["AzureWebJobsStorage"]

OUTPUT_BLOB_CONTAINER = 'openaq-output'
TEMP_FOLDER_TEMPLATE = 'openaq/temp/{}'
OUTPUT_FOLDER_TEMPLATE = 'openaq/output/{}'

prev_day = datetime.utcnow() - timedelta(days=1)
prev_day = prev_day.strftime('%Y-%m-%d')
log = logging.getLogger()


def download_intermediate_results(filename):
    """Download a file from blob container
    Parameters
    ----------
    filename: string, required
        Name of the file in blob container source bucket (OpenAQ intermediate results)
    Returns
    -------
    processed_file: string
        Local path to downloaded file
    """

    try:
        blob_name = TEMP_FOLDER_TEMPLATE.format(filename)
        processed_file = os.path.join(
            tempfile.gettempdir(), os.path.basename(filename))
        blob = BlobClient.from_connection_string(
            conn_str=connection_str, container_name=OUTPUT_BLOB_CONTAINER, blob_name=blob_name)

        with open(processed_file, "wb") as my_blob:
            blob_data = blob.download_blob()
            blob_data.readinto(my_blob)

    except Exception as e:
        log.error(f'Unable to download result file: {filename}')
        log.debug(e)
        raise
    return processed_file


def process_intermediate_results(dataframes):
    """Combine hourly air quality ratings and calculate daily ratings for each location.
    Parameters
    ----------
    dataframes: list of Pandas dataframes, required
        List of dataframes with hourly air quality ratings
    Returns
    -------
    summary_stats: Pandas dataframe
        Daily summary of air quality ratings
    """

    try:
        # combine into single dataframe
        data = pd.concat(dataframes, sort=False)

        data['date.utc'] = pd.to_datetime(data['date.utc'], utc=True)

        # calculate stats
        summary_stats = data.set_index('date.utc').groupby([pd.Grouper(
            freq='D'), 'country', 'city', 'location']).agg([np.nanmin, np.nanmax, np.nanmean])
        summary_stats.columns = ["_".join(x)
                                 for x in summary_stats.columns.ravel()]

        # format the columns
        summary_stats = summary_stats.reset_index()
        # there is occasionally historic data in the source
        summary_stats = summary_stats[summary_stats['date.utc'].dt.date.astype(
            str) == prev_day]
        summary_stats['date.utc'] = summary_stats['date.utc'].dt.date
        summary_stats.drop_duplicates(inplace=True)
        new_columns = {'date.utc': 'date',
                       'bc_nanmin': 'bc_min',
                       'bc_nanmax': 'bc_max',
                       'bc_nanmean': 'bc_mean',
                       'co_nanmin': 'co_min',
                       'co_nanmax': 'co_max',
                       'co_nanmean': 'co_mean',
                       'no2_nanmin': 'no2_min',
                       'no2_nanmax': 'no2_max',
                       'no2_nanmean': 'no2_mean',
                       'o3_nanmin': 'o3_min',
                       'o3_nanmax': 'o3_max',
                       'o3_nanmean': 'o3_mean',
                       'pm10_nanmin': 'pm10_min',
                       'pm10_nanmax': 'pm10_max',
                       'pm10_nanmean': 'pm10_mean',
                       'pm25_nanmin': 'pm25_min',
                       'pm25_nanmax': 'pm25_max',
                       'pm25_nanmean': 'pm25_mean',
                       'so2_nanmin': 'so2_min',
                       'so2_nanmax': 'so2_max',
                       'so2_nanmean': 'so2_mean'
                       }
        summary_stats.rename(columns=new_columns, inplace=True)
    except Exception as e:
        log.error("Error processing data")
        log.debug(e)
        raise

    return summary_stats


def upload_final_results(results):
    """Upload a file to blob container
    Parameters
    ----------
    results: string, required
        Name of the local file with final results
    """

    # upload to target Azure Blob Container
    try:
        results_path = os.path.join(tempfile.gettempdir(), results)
        blob_name = OUTPUT_FOLDER_TEMPLATE.format(results)
        blob = BlobClient.from_connection_string(
            conn_str=connection_str, container_name=OUTPUT_BLOB_CONTAINER, blob_name=blob_name)
        with open(results_path, "rb") as data:
            blob.upload_blob(data)

        log.info("Uploaded final results to blob container {}, path: ".format(OUTPUT_BLOB_CONTAINER) + OUTPUT_FOLDER_TEMPLATE.format(results))
    except Exception as e:
        log.error(f'Unable to upload final results: {results}')
        log.debug(e)
        raise


def main(event):
    dataframes = []
    temp_files = []
    # download files locally
    for item in event:
        temp_files.append(item['processed_file'])
        intermediate_result = download_intermediate_results(item['processed_file'])
        # read each file and store as Pandas dataframe
        with gzip.GzipFile(intermediate_result, 'r') as data_file:
            raw_json = json.loads(data_file.read())
            df = pd.DataFrame.from_dict(raw_json)
            dataframes.append(df)

    summary_stats = process_intermediate_results(dataframes)
    # write to file
    output_file_name = '{}.csv.gz'.format(prev_day)
    output_file = os.path.join(tempfile.gettempdir(), output_file_name)

    summary_stats.to_csv(
        output_file,
        compression='gzip',
        index=False,
        header=True)

    upload_final_results(output_file_name)

    return {
        "message": "Successfully processed data for {}".format(prev_day),
        "intermediate_files": temp_files,
        "output_file": "{}/".format(OUTPUT_BLOB_CONTAINER) + OUTPUT_FOLDER_TEMPLATE.format(output_file_name)
        }
