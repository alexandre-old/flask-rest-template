from . import users, utils
import flask
import datetime


def define_jwt_handlers(jwt):
    """TODO: Docstring for define_jwt_handlers.

    :jwt: TODO
    :returns: TODO

    """

    @jwt.authentication_handler
    def authtenticate(username, password):
        """TODO: Docstring for authtenticate
        :returns: TODO

        """
        user = users.models.User.objects(username=username).first()
        if user and utils.verify_password(password, user.password):
            return user
        else:
            return None


    @jwt.user_handler
    def load_user(payload):
        """TODO: Docstring for load_user
        :returns: TODO

        """
        user = users.models.User.objects(id=payload['user_id']).first()
        if user:
            return user
        return {'error': 'Houston, we have a problem!'}


    @jwt.error_handler
    def error_handler(error):
        """TODO: Docstring for error_handler
        :returns: TODO

        """
        return 'Auth Failed', 400


    @jwt.payload_handler
    def make_payload(user):
        """TODO: Docstring for .
        :returns: TODO

        """
        return {
            'user_id': str(user.id),
            'exp': (
                datetime.datetime.utcnow() +
                flask.current_app.config['JWT_EXPIRATION_DELTA']).isoformat()
        }
