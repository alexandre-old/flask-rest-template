import bson


def is_a_valid_objectid(objid):
    """Verify if a string is a valid value as ObjectId

    :objid: a string value.
    :returns: True or False

    """
    return bson.objectid.ObjectId.is_valid(objid)
