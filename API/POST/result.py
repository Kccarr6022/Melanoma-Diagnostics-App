#import prediction_function
import boto3, botocore
from dotenv import load_dotenv
from datetime import date
import psycopg2
import json
import os

# load environment
load_dotenv()

# connect to database
conn = psycopg2.connect(
    host=os.environ['RDS_HOST'],
    database=os.environ['RDS_DB'],
    user=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'])
cursor = conn.cursor()

entry = {
    'id' : None,
    'name' : '',
    'result': None,
    'date' : date.today()
}


def lambda_handler(event, context):

    # insert post to database
    SQL = f"INSERT INTO result VALUES({entry['id']}, '{entry['name']}', {entry['result']}, '{entry['date']}')"
    cursor.execute(SQL)
    record = cursor.fetchall()
    print(record)
    conn.commit()

    # body of response
    response_body = {}
    response_body['message'] = f"Added {entry['name']}'s data to the database"

    # construct response
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(response_body)

    return response_object