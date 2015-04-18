# Flask REST Template

[![Code Health](https://landscape.io/github/alexandre/flask-rest-template/master/landscape.svg?style=flat)](https://landscape.io/github/alexandre/flask-rest-template/master)

A template or boilerplate for a Flask REST application.

# About the default packages/libs:

The initial libs are:
* Flask-Restful ->
* Flask-JWT ->
* Py.test ->
* MongoEngine or SQLAlchemy ->
* Gunicorn ->

# About the initial features:

* \[TODO\] The template starts with a basic auth using JWT and a really simple CRUD for users. The CRUD is because I would like a way to create an example using blueprints.
* \[ TODO \] An initial approach to use py.test with a simple mock module.
* \[ TODO \] A simples doc module with basic files about the auth, setups and etc.

Basicly, this features are just examples.

# About the branches:

* __master__: The master branch is a template using MongoEngine and Heroku config. This branch also a simple version, for example, without celery.
* \[TODO\] __master-with-sqlalchemy__: As the name suppos, this branch is just the master branch using sqlalchemy.
* \[TODO\] __mongo-celery-nginx__: This branch is the master branch with an initial config to use celery. Also there is some tips to set up this app using Nginx.
* \[TODO\] __sqlalchemy-celery-nginx__: ...you know...using sqlalchemy.

This branches are specific branches, beyond this ones there are the workflow branches (development, release, issue/feature).

# About the license:

The public domain license is fair enough for this project - union of repos that I saw, questions that I read in the Stack
Overflow or tweets (and I'm ok to share my ideas with this license). The most part of inspirations are using the MIT 
license, but if I choose another license, I'm sure that would be GPL/AGPL V3. =]

# About the inspirations:

* Ideas and answers >> #pocoo IRC channel;
* cookiecutter-flask;
* Flask Snippets;
* Flask-restful-example;
* [What the Flask](http://pythonclub.com.br/tag/what-the-flask.html) a tutorial in portuguese by [Bruno Rocha](https://github.com/rochacbruno)
* Flaskbook by [Miguel Grinberg](https://github.com/miguelgrinberg)
* Some questions in Stack Overflow or tweets that I don't have a link. =P

# Python2 or Python3 ?

I'm using __Python 3.4.X__.

# P.S:

 I am not a native english speaker, so I'm sorry if there are too many mistakes. =P
