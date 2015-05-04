from bson.objectid import ObjectId
from app.users import controllers
from tests import clear_db


def test_is_an_available_username_with_available_user(app):
    clear_db()
    assert controllers.is_an_available_username(username='available') is True


def test_is_an_available_username_with_unavailable_user(app, mock_user):
    clear_db()
    mock_user(username='unavailable', password='unavailable')

    assert controllers.is_an_available_username('unavailable') is False


def test_get_users_no_data(app):
    assert controllers.get_users() == {'no-data': ''}


def test_get_users_with_data(app, mock_user):
    clear_db()
    user = mock_user()
    expected = {
        'success': [{
            'id': str(user.id),
            'username': user.username
        }]
    }

    assert controllers.get_users() == expected


def test_get_users_with_data_and_specific_username(app, mock_user):
    clear_db()
    user = mock_user()
    expected = {
        'success': [{
            'id': str(user.id),
            'username': user.username
        }]
    }

    assert controllers.get_users(username=user.username) == expected


def test_create_user_with_invalid_username(app, mock_user):
    clear_db()
    user = mock_user()
    username, password = user.username, 'password'
    expected = {
        'error': 'The user {!r} already exists.'.format(user.username)
    }

    assert controllers.create_or_update_user(username, password) == expected


def test_create_user_with_valid_username(app):
    clear_db()
    username, password = 'valid user', 'password'

    assert 'created' in controllers.create_or_update_user(username, password)


def test_update_user_with_valid_username(app, mock_user):
    clear_db()
    user = mock_user()
    id, username, password = str(user.id), 'updated', 'password'

    assert 'updated' in controllers.create_or_update_user(
        username, password, user_id=id)


def test_delete_user_with_invalid_id(app):

    expected = {'error': 'Invalid user id.'}
    assert controllers.delete_user(str(ObjectId())) == expected


def test_delete_user_with_valid_id(app, mock_user):

    user = mock_user()
    expected = {'deleted': 'User deleted'}

    assert controllers.delete_user(str(user.id)) == expected
