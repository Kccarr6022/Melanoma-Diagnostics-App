###############################################
# App
# --------------------
#
# This file is referenced by manage.py.
#
###############################################

# Import the required packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from dotenv import load_dotenv
import os

# loads environment variables
load_dotenv()

# inits database, ma schemas, and cross orgin requests 
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

# private database keys to connect
DB_URL = os.environ.get('DB_HOST')
DB = os.environ.get('DB')
DB_USER = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
CONNECTION_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_URL}/{DB}"


# DB_HOST=melanomadatabase.csxmxcpl4fab.us-east-2.rds.amazonaws.com
# DB=melanomadatabase
# DB_USERNAME=melanoma
# DB_PASSWORD=melanoma_app

# creates app and returns app with configuration
def create_app():
    # Initialize application
    """Application-factory pattern"""
    app = Flask(__name__)

    # Database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 400 # sets to 100 default for production (20 for our development)
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 1000 # prevent crashes
    app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_URL
    db = SQLAlchemy(app)


    # init db and ma
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    return app
