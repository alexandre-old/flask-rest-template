from app.extensions import db


class User(db.Document):

    """User model """

    username = db.StringField()
    password = db.StringField()

    def to_json2(self):
        """Returns a json representantion of the user.
        :returns: a json object.

        """

        return {
            'id': str(self.id),
            'username': self.username
        }
