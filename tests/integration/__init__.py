import json


def get_jwt_auth_header(username, password, client):
    """Executes the process to create a jwt header. It's just a way to avoid
    repeated code in tests.
    :returns: a dict with the header 'Authorization' and a valid value.

    """

    payload = {'username': username, 'password': password}
    auth_response = client.post('/api/auth', data=json.dumps(payload))

    if auth_response.status_code != 200:
        raise RuntimeError(auth_response.data.decode('utf-8'))

    return {
        'Authorization': 'Bearer {}'.format(
            json.loads(auth_response.data.decode('utf-8'))['token'])
    }


def jrequest(method, url, client, headers={}, data=None):
    """Executes json requests.

    :method: 'GET', 'POST', 'PUT' or 'DELETE' (case sensitive)
    :url: a string object (valid as url)
    :client: flask.Flask.test_client
    :headers: Optional headers.
        As default uses Content-Type: application/json
    :data: Optional data for POST or PUT requests
    :returns: the request reponse.

    """

    allowed_methods = {
        'GET': lambda: client.get(url, headers=headers),
        'POST': lambda: client.post(url, headers=headers, data=data),
        'PUT': lambda: client.put(url, headers=headers, data=data),
        'DELETE': lambda: client.delete(url, headers=headers),
    }

    if 'Content-Type' not in headers:
        headers.update({'Content-Type': 'application/json'})

    return allowed_methods[method]()
