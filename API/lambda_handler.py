import json
import psycopg2

print('Loading function')

def lambda_handler(event, context):
    #1. Parse out query string params
    transactionId = event['queryStringParameters']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print(f"Transaction Id: {transactionId}")
    print(f"Transaction Type: {transactionType}")
    print(f"Transaction Amount: {transactionAmount}")

    #2. constructs body of response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello from lambda land'

    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    return responseObject