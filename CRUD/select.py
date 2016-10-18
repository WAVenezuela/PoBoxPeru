from flask import Flask
from flask_restful import Resource, Api

class Select(Resource):
    def get(self):
        return {'Msg':'This is a SelectS'}
    
    def post(self):
        return {'msg': 'This is a insert'}