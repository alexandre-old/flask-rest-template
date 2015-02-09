import pytest
from app import parsers


def test_objectid_parser_invalid_objid():
    """TODO: Docstring for test_objectid_parser.
    :returns: TODO

    """
    with pytest.raises(ValueError) as error:
        parsers.objectid_parser("HAHHAHAHHA")

    assert str(error.msg) == "Invalid ObjectId"
