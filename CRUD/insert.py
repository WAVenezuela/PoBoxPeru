from flask import Flask
from flask_restful import Resource, Api

class Insert:
    def post(self):
        return {'msg': 'This is a insert'}