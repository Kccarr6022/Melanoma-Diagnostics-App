#import prediction_function
import boto3, botocore
from dotenv import load_dotenv
from datetime import date
import psycopg2
import json
import os

load_dotenv()
conn = psycopg2.connect(
    host=os.environ['RDS_HOST'],
    database=os.environ['RDS_DB'],
    user=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'])
cursor = conn.cursor()

entry = {
    'id' : 2,
    'name' : '',
    'result': None,
    'date' : date.today()
}

SQL = "SELECT * FROM results"
cursor.execute(SQL)
record = cursor.fetchall()
print(record)
conn.commit()


def lambda_handler(event, context):

    #2. constructs body of response object
    response_body = {
        "result" : entry #prediction_function(image)
    }

    #3. Construct http response object
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(response_body)

    return response_body