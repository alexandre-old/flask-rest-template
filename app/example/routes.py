from . import views


def register_resources(api):
    """TODO: Docstring for register_resources.

    :api: TODO
    :returns: TODO

    """

    api.add_resource(views.ExampleAPI, '/example')

    return None
