import json
import os


class Config(object):

    """Docstring for Config. """

    _settings = None
    _db_connection = None

    def __init__(self, settings_file):
        """TODO: Docstring for __init__.

        :settings_file: TODO
        :returns: TODO

        """
        self._set_settings(settings_file)
        self._set_db_connection()

    def _set_settings(self, settings_file_path):
        """TODO: Docstring for _set_settings.

        :settings_file: TODO
        :returns: TODO

        """
        if not os.access(settings_file_path, os.R_OK):
            raise ValueError('Invalid settings file path')

        with os.open(settings_file_path) as settings_file:
            self._settings = json.loads(settings_file)

    def _set_db_connection(self):
        """TODO: Docstring for _set_db_connection.
        :returns: TODO

        """
        if not self._settings:
            raise ValueError('Invalid Settings.')

        self._db_connection = self._settings['db_connection']

    @property
    def db_connection(self):
        """TODO: Docstring for db_connection.
        :returns: TODO

        """
        return self._db_connection


class DevelopmentConfig(Config):

    """Docstring for DevelopmentConfig. """

    def __init__(self, app):
        """TODO: to be defined1. """
        app.debug = True
        return super(DevelopmentConfig, self).__init__('development.json')


class TestingConfig(Config):

    """Docstring for TestingConfig. """

    def __init__(self, app):
        """TODO: to be defined1. """
        return super(TestingConfig, self).__init__('testing.json')


class ProductionConfig(Config):

    """Docstring for ProductionConfig. """

    def __init__(self, app):
        """TODO: to be defined1. """
        return super(ProductionConfig, self).__init__('production.json')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
