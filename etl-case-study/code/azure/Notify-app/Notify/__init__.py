import logging
import os

import azure.functions as func
from azure.storage.queue import QueueClient

connection_str = os.environ["AzureWebJobsStorage"]
QUEUE_NAME = "results-queue"

def main(myblob: func.InputStream):
    queue_client = QueueClient.from_connection_string(connection_str, QUEUE_NAME)
    message = {
        "name": myblob.name,
        "uri": myblob.uri,
        "message": "The blob was successfully uploaded"
    }    

    queue_client.send_message(message)