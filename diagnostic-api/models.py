###############################################
# # Models
# # --------------------
# # This file houses the definitions for all the database models via SQLAlchemy.
# #
# ###############################################

# from enum import unique
# from sqlalchemy import true
# from app import db,ma
# from datetime import datetime

# ####################################
# #
# # Tables
# #
# ####################################

# class Results(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     confidence_level = db.Column(db.Integer, nullable=False)
#     date = db.Column(db.DateTime(), nullable=False)

#     def __repr__(self):
#         return "<Articles %r>" % self.title

# ####################################
# #
# # Marshmallow Schema
# #
# ####################################


# # Generate marshmallow Schemas from your models
# class ResultsSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         model = Results
#         fields = ("id","name", "confidence_level", "date")
#         load_instance = True

# result_schema = ResultsSchema()
# results_schema = ResultsSchema(many=True)