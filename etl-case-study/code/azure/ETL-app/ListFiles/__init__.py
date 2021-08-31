import boto3
from botocore import UNSIGNED
from botocore.client import Config

import logging
from datetime import datetime, timedelta

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

OPENAQ_BUCKET = 'openaq-fetches'
DATA_PREFIX = 'realtime-gzipped'
CHUNK_SIZE = 6

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


def main(event):
    log.info(f"Processing data for: {prev_day}")
    file_names = get_file_inventory()
    chunks = [file_names[i:i + CHUNK_SIZE]
            for i in range(0, len(file_names), CHUNK_SIZE)]

    return {
        "value": chunks,
        "message": "Init phase complete"}