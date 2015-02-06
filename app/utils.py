import bson


def is_an_objectid_valid(str):
    """Verify if a string is a valid value as ObjectId

    :str: a string value.
    :returns: True or False

    """
    return bson.objectid.ObjectId(str).is_valid()
