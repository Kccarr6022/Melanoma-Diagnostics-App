from ..prediction_function import *
import json


print('Loading function')

result = 0

def test(file = None) -> int:
    return 1

def lambda_handler(event, context):
    #1. Parse out query string params
    transactionId = event['queryStringParameters']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print(f"Transaction Id: {transactionId}")
    print(f"Transaction Type: {transactionType}")
    print(f"Transaction Amount: {transactionAmount}")

    #2. constructs body of response object
    result = test(None)
    transactionResponse = {
        "result" : result
    }

    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject
lambda_handler()