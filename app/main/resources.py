from flask_restful import Resource
from flask import jsonify

class IndexResource(Resource):
    def get(self):
        return jsonify({"messgae":"Hello World"})
