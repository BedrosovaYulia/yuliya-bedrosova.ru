import json
import os
from bitrix24 import Bitrix24

def lambda_handler(event, context):
    # TODO implement
    print(event['queryStringParameters'])
    
    domain=os.environ['domain']
    key=os.environ['key']
    bx24 = Bitrix24(domain, user_id=1)
    
    lead_data = {
        "fields" : {
          "TITLE": event['queryStringParameters']['name'],
          "NAME" : event['queryStringParameters']['name'],
          "EMAIL": [{ "VALUE": event['queryStringParameters']['email'], "VALUE_TYPE": "WORK" }],
          "COMMENTS":event['queryStringParameters']['message']
          }
        }
        
    result = bx24.call_webhook('crm.lead.add', key, params=lead_data)
    print(result)

    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lam")
    }
