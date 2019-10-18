from flask import request, Response
from flask_restplus import Resource, Namespace

import unidecode
import json

from app.engine.query import Query
from app.engine.score import ScoreInterface


api = Namespace('suggestions', description='All valid suggestions')

@api.route('/')
class Suggestions(Resource):
    @api.doc('list_of_valid_suggestions')
    def get(self):
        query = Query(request.args)
        data = ScoreInterface().run(query)
        response = {
            'suggestions': data
        }

        response = json.dumps(response, ensure_ascii=False)
        response = Response(response, 
            content_type="application/json; charset=utf-8")
        return response
