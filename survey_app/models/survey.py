from werkzeug import datastructures
from survey_app.config.mysqlconnection import connectToMySQL
from survey_app import app
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.score = data['score']

    @classmethod
    def savingform(cls,data):
        query = "INSERT INTO survey (name,location,language,score,comment) VALUES (%(name)s,%(location)s,%(language)s,%(score)s,%(comment)s);"
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return results

    @classmethod
    def getsubmission(cls,num):
        query = "SELECT * FROM survey WHERE id = %(id)s;"
        data = {
            'id' : num
        }
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        submission = []
        for line in results:
            submission.append(Survey(line))
        return submission

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Please provide a valid name")
            is_valid = False
        if len(data['location']) < 2:
            flash("Please select a location")
            is_valid = False
        if len(data['language']) < 2:
            flash("Please select a language")
            is_valid = False
        if int(data['score']) == 0:
            flash("Please select a valid rating option")
            is_valid = False
        if len(data['comment']) < 2:
            flash("Please provide a valid comment")
            is_valid = False
        return is_valid
