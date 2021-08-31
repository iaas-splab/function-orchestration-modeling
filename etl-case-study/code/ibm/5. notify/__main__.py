import requests
import sys

def main(params):
    host = 'host_name'
    queue_manager = 'queue_manager_name'
    queue_name = 'queue_name'
    endpoint_placeholder = 'https://HOST/ibmmq/rest/v1/messaging/qmgr/QUEUE_MANAGER/queue/QUEUE_NAME/message'
    
    auth_string = params['BASIC_AUTH_STRING']    
    
    if 'HOST' in params and type(params['HOST']) == str:
        host = params['HOST']
    endpoint = endpoint_placeholder.replace('HOST', host)
    
    if 'QUEUE_MANAGER' in params and type(params['QUEUE_MANAGER']) == str:
        queue_manager = params['QUEUE_MANAGER']
    endpoint = endpoint.replace('QUEUE_MANAGER', queue_manager)

    if 'QUEUE_NAME' in params and type(params['QUEUE_NAME']) == str:
        queue_name = params['QUEUE_NAME']
    endpoint = endpoint.replace('QUEUE_NAME', queue_name)
    
    req_headers = {
        "Authorization": "Basic " + auth_string, 
        "Content-Type":"application/json", 
        "ibm-mq-rest-csrf-token": "ignored_because_basicauth_is_used"
    }
    
    payload = {"event": "TBD"}
    if 'notification' in params:
        payload = params['notification']

    response = requests.post(endpoint, headers=req_headers, json=payload)
    message = response.text
    if not message:
        message = "Message successfully sent to the queue " + queue_name
    
    return { "result": message }