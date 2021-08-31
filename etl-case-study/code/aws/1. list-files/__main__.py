import boto3
import os
from botocore import UNSIGNED
from botocore.client import Config

from datetime import datetime, timedelta

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

OPENAQ_BUCKET = 'openaq-fetches'
DATA_PREFIX = 'realtime-gzipped'

# look for all files from previous day
prev_day = datetime.utcnow() - timedelta(days=1)
prev_day = prev_day.strftime('%Y-%m-%d')
prefix = '{}/{}/'.format(DATA_PREFIX, prev_day)

def get_file_inventory():
    try:
        response = s3.list_objects_v2(Bucket=OPENAQ_BUCKET, Prefix=prefix)
        file_names = [item['Key'] for item in response['Contents']]
    except Exception as e:
        print('Unable to list OpenAQ files')
        raise
    return file_names


def main(event, context):
    # default chunk size if no value is provided in the input
    chunk_size = 12

    if 'chunk_size' in event: 
        if type(event['chunk_size']) == int:
            chunk_size = event['chunk_size']
    
    file_names = get_file_inventory()
    chunks = [file_names[i:i + chunk_size]
            for i in range(0, len(file_names), chunk_size)]
    
    return {
        "value": chunks, 
        "message": "Init phase complete"}