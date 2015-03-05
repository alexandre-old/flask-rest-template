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
    """Define a dict with the Flask app and db connection object
    :returns: a dict

    """
    return {'app': app, 'db': db}


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(port=5000, host='0.0.0.0'))


if __name__ == "__main__":
        manager.run()
