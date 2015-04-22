from flask import Blueprint
from flask.ext.restful import Api
from . import resources


blueprint = Blueprint('users', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(resources.UsersAPI, '/users')
