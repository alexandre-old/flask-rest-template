from flask import Blueprint
from flask.ext.restful import Api


blueprint = Blueprint('users', __name__)
api = Api(prefix='/api')
api.init_app(blueprint)
