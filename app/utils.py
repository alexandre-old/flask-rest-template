import bson


def is_a_valid_object_id(object_id):
    """Verify if the value is valid as an object id.
    :object_id: a string object
    :returns: True or False

    """
    return bson.objectid.ObjectId.is_valid(object_id)
