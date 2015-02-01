from app.extensions import db


class Example(db.Document):

    """Docstring for Example. """

    foo = db.StringField()
    bla = db.IntField()
    ble = db.StringField()

    def to_json(self):
        """TODO: Docstring for to_json.
        :returns: TODO

        """

        return {
            'id': str(self._id),
            'foo': self.foo,
            'bla': self.bla,
            'ble': self.ble
        }
