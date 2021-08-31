import ibm_boto3
from ibm_botocore import UNSIGNED
from ibm_botocore.client import Config

import logging
import os
from datetime import datetime, timedelta

s3 = ibm_boto3.client('s3', config=Config(signature_version=UNSIGNED))

OPENAQ_BUCKET = 'openaq-fetches'
DATA_PREFIX = 'realtime-gzipped'

# look for all files from previous day
prev_day = datetime.utcnow() - timedelta(days=1)
prev_day = prev_day.strftime('%Y-%m-%d')
prefix = '{}/{}/'.format(DATA_PREFIX, prev_day)

log = logging.getLogger()


def get_file_inventory():
    """List files in OpenAQ bucket for previous day
    Returns
    -------
    file_names: list
        List of air quality files to be processed
    """

    try:
        response = s3.list_objects_v2(Bucket=OPENAQ_BUCKET, Prefix=prefix)
        file_names = [item['Key'] for item in response['Contents']]
        log.info(f"Total files to process: {len(file_names)}")
    except Exception as e:
        log.error(f'Unable to list OpenAQ files: {response}')
        log.debug(e)
        raise
    return file_names


def main(params):
    # default chunk size if no value is provided in the input
    chunk_size = 12

    if 'chunk_size' in params and type(params['chunk_size']) == int:
        chunk_size = params['chunk_size']

    file_names = get_file_inventory()
    chunks = [file_names[i:i + chunk_size]
              for i in range(0, len(file_names), chunk_size)]

    return {
        "value": chunks,
        "message": "Init phase complete"}
