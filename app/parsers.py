from app import utils


def val_objectid(objid):
    """TODO: Docstring for val_objectid.

    :objid: A string that should represent an ObjectId
    :returns: objid

    """
    if utils.is_an_objectid_valid(objid) is False:
        raise ValueError("Invalid ObjectId")

    return objid
