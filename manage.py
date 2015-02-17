#!/usr/bin/env python

from app import create_app
from flask.ext.script import Manager, Shell, Server
from app.extensions import db
import os


# create an app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# activate the manager
manager = Manager(app)


def make_shell_context():
    """TODO: Docstring for make_shell_context.
    :returns: TODO

    """
    return {'app': app, 'db': db}


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(port=5000, host='0.0.0.0'))


if __name__ == "__main__":
        manager.run()
