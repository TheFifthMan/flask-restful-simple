from flask import Blueprint
from flask_restful import Api
auth = Blueprint('auth',__name__)
api = Api(auth)


from .resources import RegisterResource
api.add_resource(RegisterResource,'/register')
