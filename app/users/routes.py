from . import views


def register_resources(api):
    """TODO: Docstring for register_resources.

    :api: TODO
    :returns: TODO

    """
    api.add_resource(views.UsersAPI, '/users', endpoint='users')
    api.add_resource(views.PersonalAPI, '/personal', endpoint='personal')

    return None
