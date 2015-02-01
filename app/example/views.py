from flask.ext.restful import Resource
from . import controllers
from flask_jwt import jwt_required


class ExampleAPI(Resource):

    """Docstring for ExampleAPI."""

    @jwt_required()
    def get(self):
        """TODO: Docstring for get.
        :returns: TODO

        """
        pass

    @jwt_required()
    def post(self):
        """TODO: Docstring for post.
        :returns: TODO

        """
        pass

    def options(self):
        """TODO: Docstring for options.
        :returns: TODO

        """

        # useful for crossdomain apps
        pass
