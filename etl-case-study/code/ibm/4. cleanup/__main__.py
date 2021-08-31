import ibm_boto3
import ibm_botocore
from ibm_botocore.client import Config
from ibm_botocore import UNSIGNED

import os
import logging

IAM_API_KEY = os.environ.get('__OW_IAM_NAMESPACE_API_KEY')
ACTIVATION_ID = os.environ.get('__OW_ACTIVATION_ID')
ENDPOINT = 'https://s3.private.eu-de.cloud-object-storage.appdomain.cloud'
COS_OUTPUT_BUCKET = 'openaq-output'

ibm_cos = ibm_boto3.client("s3",
    ibm_api_key_id=IAM_API_KEY,
    config=Config(signature_version="oauth"),
    endpoint_url=ENDPOINT
)

log = logging.getLogger()

def delete_intermediate_results(intermediate_files):
    """Delete files from IBM Cloud Object Storage
    Parameters
    ----------
    intermediate_files: list, required
        List of IBM Cloud Object Storage bucket files with intemediate results
    """

    try:
        log.info(
            ibm_cos.delete_objects(
                Bucket=COS_OUTPUT_BUCKET,
                Delete={'Objects': intermediate_files}))
    except ibm_botocore.exceptions.ClientError as e:
        log.error(f'Unable to delete intermediate results')
        log.debug(e)
        raise

def main(event):
    # delete from COS bucket
    delete_intermediate_results(event['intermediate_files'])

    return {
        "message": "Successfully deleted intermediate files", 
        "results": f'Download results here {event["output_file"]}'
    }