from app.users import controllers


def test_get_user_invalid_filter(app_db):
    """TODO: Docstring for .

    :id: TODO
    :returns: TODO

    """
    controller = controllers.UserController()
    result = controller.get_user({'invalid_attr': 'invalid value'}).keys()

    assert 'error' in result


def test_get_user_valid_username_with_mock(app_db, mock_user):
    """TODO: Docstring for test_get_user_valid_username.

    :arg1: TODO
    :returns: TODO

    """
    controller = controllers.UserController()
    result = controller.get_user({'username': 'mockuser'}).keys()

    assert 'success' in result


def test_get_user_valid_username_without_mock(app_db):
    """TODO: Docstring for test_get_user_valid_username_without_mock.

    :app_db: TODO
    :returns: TODO

    """
    controller = controllers.UserController()
    result = controller.get_user({'username': 'mockuser'}).keys()

    assert 'no-data' in result
