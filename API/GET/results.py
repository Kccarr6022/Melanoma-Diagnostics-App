from dotenv import load_dotenv
import psycopg2
import json
import os

#environment variables
load_dotenv()

#database connection
conn = psycopg2.connect(
    host=os.environ['RDS_HOST'],
    database=os.environ['RDS_DB'],
    user=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'])
cursor = conn.cursor()


def lambda_handler(event, context):

    # get results
    SQL = "SELECT * FROM results"
    cursor.execute(SQL)
    records = cursor.fetchall()


    # construct http response object
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(records)

    return response_object