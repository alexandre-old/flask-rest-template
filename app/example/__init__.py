from flask import Blueprint
from flask.ext.restful import Api
from . import routes


blueprint = Blueprint('example', __name__)
api_example = Api(blueprint, prefix='/api')

routes.register_resources(api_example)
