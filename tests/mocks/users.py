import pytest
from app import models, helpers


@pytest.yield_fixture(scope='function')
def mock_user():
    """Returns a function (clojuse) to createa a mock.
    """

    user = None

    def make_mock_user(username=None, password=None):
        """The real mock. Creates a object users.models.User .All parameters
        are optionals, by default uses the username 'mock-user', the password
        is the same value.

        :username: a string object.
        :password: a string object
        :returns: an users.models.User object

        """

        nonlocal user

        user = models.User(
            username=username or 'mock-user',
            password=helpers.encrypt_password(password or 'mock-user')
        ).save()

        return user

    yield make_mock_user

    user.delete() if user else None
