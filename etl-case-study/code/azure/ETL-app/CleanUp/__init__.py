from azure.storage.blob import ContainerClient

import os
import logging

connection_str = os.environ["AzureWebJobsStorage"]
OUTPUT_BLOB_CONTAINER = 'openaq-output'
TEMP_FOLDER_TEMPLATE = 'openaq/temp/{}'

container_client = ContainerClient.from_connection_string(conn_str=connection_str, container_name=OUTPUT_BLOB_CONTAINER)

log = logging.getLogger()

def delete_intermediate_results(intermediate_files):
    """Delete files from Blob Container
    Parameters
    ----------
    intermediate_files: list, required
        List of files with intemediate results
    """

    try:
        for filename in intermediate_files:
            blob_name = TEMP_FOLDER_TEMPLATE.format(filename)
            container_client.delete_blob(blob=blob_name)
    except Exception as e:
        log.error(f'Unable to delete intermediate results')
        log.debug(e)
        raise

def main(event):
    delete_intermediate_results(event['intermediate_files'])

    return {
        "message": "Successfully deleted intermediate files", 
        "results": f'Download results from {event["output_file"]}'}