from . import development, testing, production


def set_app_config_keys(app, settings):
    """Load all flask.Flask config vars.

    :app: a flask.Flask object
    :settings: a module with config vars
    :returns: None

    """
    # create a unique dict with all config vars
    all_config_vars = dict(
        list(settings.FLASK_VARS.items()) +
        list(settings.FLASK_JWT_VARS.items()) +
        list(settings.DB_CONNECTION.items()) +
        list(settings.PASSLIB.items())
    )

    for key, value in all_config_vars.items():
        app.config[key] = value


def development_config(app):
    """Call the function responsable by load config vars
    using 'development' settings.

    :app: a flask.Flask object
    :returns: None

    """
    set_app_config_keys(app, development)


def testing_config(app):
    """Call the function responsable by load config vars
    using 'testing' settings.

    :app: a flask.Flask object
    :returns: None

    """
    set_app_config_keys(app, testing)


def production_config(app):
    """Call the function responsable by load config vars
    using 'production' settings.

    :app: a flask.Flask object
    :returns: None

    """
    set_app_config_keys(app, production)

# Yep, I know I could use lambdas...
config = {
    'development': development_config,
    'testing': testing_config,
    'production': production_config,
    'default': development_config,
}
