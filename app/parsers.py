from app import utils


def objectid_parser(objid):
    """TODO: Docstring for val_objectid.

    :objid: A string that should represent an ObjectId
    :returns: objid

    """
    if utils.is_a_valid_objectid(objid) is False:
        raise ValueError("Invalid ObjectId")

    return objid
