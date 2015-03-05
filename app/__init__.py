import flask
from . import extensions, users, config, auth


def create_app(config_name):
    """Flask app factory

    :config_name: a string that represents a config.
    :returns: Flask app

    """
    app = flask.Flask(__name__)

    app_conf = config.config[config_name]()

    app.config.from_object(app_conf)
    app.config['MONGODB_SETTINGS'] = app_conf.get_conn_data()

    register_extensions(app)

    register_blueprints(app)

    return app


def register_extensions(app):
    """Initialize all used extensions.

    :app: a Flask app
    :returns: just a None value (it's not important)

    """
    extensions.db.init_app(app)
    extensions.jwt.init_app(app)
    extensions.api.init_app(app)

    auth.define_jwt_handlers(extensions.jwt)
    return None


def register_blueprints(app):
    """Register all created blueprints.

    :app: a Flask app
    :returns: just a None value (it's not important)

    """
    app.register_blueprint(users.blueprint)

    return None
