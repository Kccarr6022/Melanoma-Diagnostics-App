from flask import Flask, jsonify, make_response
import psycopg2
import json
import os

app = Flask(__name__)


#database information
rds_host  = "melanomadatabase.csxmxcpl4fab.us-east-2.rds.amazonaws.com"
name = "melanoma"
password = "melanoma_app"
db_name = "melanomadatabase"

#database connection
conn = psycopg2.connect(
    host=rds_host,
    database=db_name,
    user=name,
    password=password)
cursor = conn.cursor()
print('connected to db')

@app.route("/")
def hello_from_root():

    # get results
    SQL = "SELECT * FROM results ORDER BY ID"
    cursor.execute(SQL)
    records = cursor.fetchall()

    data = json.dumps(records)

    return jsonify(test_results=records)


@app.route("/hello")
def hello():

    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
