import os
import json
import logging
import boto3
from botocore.exceptions import ClientError


QUEUE_NAME = os.environ['QUEUE_NAME']
REGION = os.environ['REGION']
sqs_client = boto3.client('sqs', region_name=REGION) 


def send_sqs_message(QueueName, msg_body):
    """ Send SQS message 
    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :return: Dictionary containing information about the sent message. If error, returns None.
    """

    # Send the SQS message
    
    sqs_queue_url = sqs_client.get_queue_url(QueueName=QueueName)['QueueUrl']
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url, MessageBody=json.dumps(msg_body))
    except ClientError as e:
        logging.error(e)
        return None
    return msg


def main(event, context):
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s')

    msg = send_sqs_message(QUEUE_NAME, event)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }