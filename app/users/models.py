from app.extensions import db


class User(db.Document):

    """User model """

    username = db.StringField()
    password = db.StringField()
