from flask import Flask
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS, cross_origin
class marketData(Resource):
    def get(self):
        result = 'result'
        return {"result" : result}


app = Flask("NuriMap")
CORS(app,resources={"/markets": {"origins" : "*"}})
api = Api(app)
api.add_resource(marketData, '/markets')


