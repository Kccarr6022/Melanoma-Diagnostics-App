###############################################
# Models
# --------------------
# This file houses the definitions for all the database models via SQLAlchemy.
#
###############################################

from sqlalchemy import ForeignKey
from createapp import db,ma

# Database classes
class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True) # authentication token
    name = db.Column(db.String(100),nullable=False)
    confidence_level = db.Column(db.Integer,nullable=True)
    date = db.Column(db.Text, nullable=False)

    def __rep__(self):
        return f"Name: {self.first_name}, {self.last_name}"

# Database schemas
class ResultsSchema(ma.Schema):
    class Meta: # symptom number, symptom, symptom value
        fields = ('id', 'name', 'confidence_level', 'date')

####################################
#
# Schema for Exporting
#
####################################
result_schema = ResultsSchema()
results_schema = ResultsSchema(many=True)