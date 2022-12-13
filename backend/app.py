###############################################
# APP Routes
# --------------------
# This file houses all the routes that hit the API and returns datbaase queries 
#
###############################################

from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from createapp import create_app,db
from dotenv import load_dotenv
from createapp import create_app, db, ma
from models import Results, result_schema, results_schema

app = create_app()

# Route to retrieve alll results from database
@app.route('/api/results', methods=['GET'])
def return_results():
    """
    Returns test result in database
    """
    results = Results.query.all()

    if not results:
        response = jsonify([]), 404
    else:
    
        results = results_schema.dump(results)
        response = jsonify(results)

    return response

# Route to retrieve alll results from database
@app.route('/api/result', methods=['GET'])
def return_result():
    """
    Returns test result in database
    """
    results = Results.query.first()

    if not results:
        response = jsonify([]), 404
    else:
    
        results = result_schema.dump(results)
        response = jsonify(results)

    return response

@app.route("/api/add", methods=["POST"])
def add_data():

    data = request.get_json()
    name = data.get('name')


    

    return jsonify(test_results=data)

# for testing
@app.route("/", methods=["GET"])
def test():

    return jsonify(message="Hello from root")


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)