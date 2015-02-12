import pytest
from app import users


@pytest.fixture(scope="function")
def mock_user(request):
    """Generate a User object with the value "mockuser"
    for username and password.

    :returns: an User object

    """
    user = users.models.User(
        username="mockuser",
        password="mockuser"
    )
    user.save()

    def del_user():
        """Delete the mock..
        :returns: None

        """
        user.delete()

    request.addfinalizer(del_user)

    return user


@pytest.fixture(scope="function")
def app_db(request):
    """TODO: Docstring for app_db.

    :request: TODO
    :returns: TODO

    """
    pass
