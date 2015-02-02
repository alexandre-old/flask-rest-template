from ..extensions import db


class User(db.Document):

    """Docstring for User. """

    username = db.StringField()
    password = db.StringField()
    active = db.BooleanField(default=True)
