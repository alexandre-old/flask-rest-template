import json
import pytest
from tests import clear_db
from . import jrequest, get_jwt_auth_header

unauthorized_scenarios = [
    ['GET', '/api/users', 'Authorization Required', 401],
]


@pytest.mark.parametrize(
    'method, url, error, status_code ', unauthorized_scenarios)
def test_unauthorized_request(method, url, error, status_code, client):

    response = jrequest(method, url, client)

    assert response.status_code == status_code
    assert json.loads(response.data.decode('utf-8'))['error'] == error


def test_get_users_without_username(client, mock_user):
    clear_db()
    user = mock_user('user', 'password')
    jwt_header = get_jwt_auth_header('user', 'password', client)

    response = jrequest('GET', '/api/users', client, jwt_header)

    expected = {
        'data': [{
            'id': str(user.id),
            'username': user.username,
        }]
    }

    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))['data'] == expected
