from mocks.mock_users import mock_user
from app import create_app
import pytest
import os


@pytest.fixture(scope='module')
def app_db(request):
    """TODO: Docstring for app_db.

    :request: TODO
    :returns: TODO

    """
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    ctx = app.app_context()

    ctx.push()

    def tear_down():
        """TODO: Docstring for tear_down.
        :returns: TODO

        """
        ctx.pop()

    request.addfinalizer(tear_down)

    return app
