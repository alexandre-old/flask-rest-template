from flask.ext.restful import Resource
from flask_jwt import jwt_required
from app import helpers
from . import controllers


class UsersAPI(Resource):

    """An API to access the user CRUD"""

    @jwt_required()
    @helpers.standardize_api_response
    def get(self, username=None):
        """HTTP GET.

        :username: a string valid as object id.
        :returns: One or all available users.

        """

        result = controllers.get_users(username)
        return result
