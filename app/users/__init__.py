from flask import Blueprint
from flask.ext.restful import Api
from . import routes


blueprint = Blueprint('users', __name__)
api_users = Api(blueprint, prefix='/api')

routes.register_resources(api_users)
