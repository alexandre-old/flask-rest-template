from ..extensions import db


class User(db.Document):

    """Docstring for User. """

    username = db.StringField()
    password = db.StringField()

    @classmethod
    def get_fields_list(self):
        """TODO: Docstring for fields.
        :returns: TODO

        """
        return list(self._fields)
