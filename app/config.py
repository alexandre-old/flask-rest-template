import os
import json
import datetime


class Config():

    """TODO: Docstring for Config. """

    _db_settings = ''
    SECRET_KEY = 'AReallySecretKey',
    JWT_AUTH_URL_RULE = '/api/auth'
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)

    def get_conn_data(self):
        """TODO: Docstring for get_conn_data.
        :returns: TODO

        """
        with open(self._db_settings, encoding='utf-8') as data:
            conn_data = json.load(data)
        return conn_data



class DevelopmentConfig(Config):

    """TODO: Docstring for DevelopmentConfig. """

    DEBUG = True

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self._db_settings = 'development_conn.json'


class TestingConfig(Config):

    """Docstring for TestingConfig. """

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self._db_settings = 'testing_conn.json'


class ProductionConfig(Config):

    """Docstring for ProductionConfig. """

    def __init__(self):
        """TODO: Docstring for __init__.
        :returns: TODO

        """
        self._db_settings = 'production_conn.json'


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}
