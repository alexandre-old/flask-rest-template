import flask
from . import extensions, users, config, auth


def create_app(config_name):
    """TODO: Docstring for create_app.

    :config_name: TODO
    :returns: TODO

    """
    app = flask.Flask(__name__)

    app_conf = config.config[config_name]()

    app.config.from_object(app_conf)
    app.config['MONGODB_SETTINGS'] = app_conf.get_conn_data()

    register_extensions(app)

    register_blueprints(app)

    return app


def register_extensions(app):
    """TODO: Docstring for register_extensions.

    :app: TODO
    :returns: TODO

    """
    extensions.db.init_app(app)
    extensions.jwt.init_app(app)
    extensions.api.init_app(app)

    auth.define_jwt_handlers(extensions.jwt)
    return None


def register_blueprints(app):
    """TODO: Docstring for register_blueprints.

    :app: TODO
    :returns: TODO

    """
    app.register_blueprint(users.blueprint)

    return None
