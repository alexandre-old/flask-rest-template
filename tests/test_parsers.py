import pytest
from app import parsers


def test_objectid_parser_invalid_objid():
    """TODO: Docstring for test_objectid_parser.
    :returns: TODO

    """
    with pytest.raises(ValueError) as error:
        parsers.objectid_parser("HAHHAHAHHA")

    assert str(error.value) == "Invalid ObjectId"


def test_objectid_parser_valid_objid():
    """TODO: Docstring for test_objectid_parser_valid_objid.
    :returns: TODO

    """
    valid_id = "54d81a1430df821df0c90f5a"
    assert parsers.objectid_parser(valid_id) == valid_id
