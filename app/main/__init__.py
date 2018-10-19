from flask import Blueprint
from flask_restful import Api
main = Blueprint('main',__name__)
api = Api(main)

# 统一管理资源路径
from .resources import IndexResource
api.add_resource(IndexResource,'/index')
