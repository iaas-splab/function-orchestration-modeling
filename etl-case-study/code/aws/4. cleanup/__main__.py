import boto3
import botocore

import os
import logging

s3 = boto3.client('s3')
RESULTS_BUCKET = os.environ['RESULTS_BUCKET']

log = logging.getLogger()

def delete_intermediate_results(intermediate_files):
    """Delete files from the S3 bucket
    Parameters
    ----------
    intermediate_files: list, required
        List of S3 files with intemediate results
    """

    try:
        s3.delete_objects(Bucket=RESULTS_BUCKET, Delete={'Objects': intermediate_files})
    except botocore.exceptions.ClientError as e:
        log.error(f'Unable to delete intermediate results')
        log.debug(e)
        raise

def main(event, context):
    # delete from the S3 bucket
    delete_intermediate_results(event['intermediate_files'])

    return {
        "message": f'Processing complete, you can download the result from {event["result_path"]}',
        "result_path": event["result_path"]
    }