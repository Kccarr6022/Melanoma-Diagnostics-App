from flask import Flask, jsonify, make_response
from dotenv import load_dotenv
import psycopg2
import json
import os

app = Flask(__name__)

#environment variables
load_dotenv()

#database connection
conn = psycopg2.connect(
    host=os.environ['RDS_HOST'],
    database=os.environ['RDS_DB'],
    user=os.environ['RDS_USERNAME'],
    password=os.environ['RDS_PASSWORD'])
cursor = conn.cursor()


@app.route("/api/result", methods=['GET'])
def respond_result():

    # get result
    SQL = "SELECT * FROM results WHERE id=(SELECT max(id) FROM results);"
    cursor.execute(SQL)
    records = cursor.fetchall()

    return json.dumps(records), 200


@app.route("/api/results", methods=['GET'])
def respond_results():

    return jsonify(message='Hello from path!')

@app.route()

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
