from flask import Flask
from flask_restful import Resource, reqparse, Api

class marketData(Resource):
    def get(self):
        result = 'result'
        return {"result" : result}


app = Flask("NuriMap")
api = Api(app)
api.add_resource(marketData, '/markets')


