from flask.ext.restful import Resource
from flask_jwt import jwt_required


class UsersAPI(Resource):

    """An API to access the user CRUD"""

    @jwt_required()
    def get(self, username=None):
        """HTTP GET.

        :username: a string valid as object id.
        :returns: One or all available users.

        """
        pass

