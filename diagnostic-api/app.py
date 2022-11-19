from flask import Flask, jsonify, make_response, request
import psycopg2
import json
import os

app = Flask(__name__)

# #database information
rds_host  = "melanomadatabase.csxmxcpl4fab.us-east-2.rds.amazonaws.com"
name = "melanoma"
password = "melanoma_app"
db_name = "melanomadatabase"

#database connection
conn = psycopg2.connect(
    host= rds_host,
    database=db_name,
    user=name,
    password=password)
cursor = conn.cursor()


@app.route("/api/results", methods=["GET"])
def return_results():

    # get results
    SQL = "SELECT * FROM results ORDER BY id"
    cursor.execute(SQL)
    records = cursor.fetchall()


    return jsonify(test_results=records)


@app.route("/api/result", methods=["GET"])
def latest_result():

     # get results
    SQL = "SELECT * FROM results ORDER BY id DESC LIMIT 1"
    cursor.execute(SQL)
    records = cursor.fetchall()


    return jsonify(latest_result=records)


@app.route("/api/add", methods=["POST"])
def add_data():

    data = request.get_json()
    

    return jsonify(test_results=data)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
