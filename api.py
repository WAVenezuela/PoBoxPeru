from flask import Flask
from flask_restful import Resource, Api
from CRUD import select,insert

app = Flask(__name__)
api = Api(app)

select = select.Select

api.add_resource(select, '/select')

if __name__ == '__main__':
    app.run(debug = True)