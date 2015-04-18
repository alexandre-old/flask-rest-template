import flask
from . import extensions, config, users


def create_app(config_name='default'):
    """TODO: Docstring for create_app.

    :config_name: TODO
    :returns: TODO

    """

    app = flask.Flask(__name__)

    # set the config vars using the config name and current_app
    config.config[config_name](app)

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


def register_blueprints(app):
    """TODO: Docstring for register_blueprints.

    :app: TODO
    :returns: TODO

    """
    app.register_blueprint(users.blueprint)
