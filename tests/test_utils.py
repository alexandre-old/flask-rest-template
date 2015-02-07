from app import utils
import pytest
import bson


p = pytest.mark.parametrize

scenarios = [
    ["apdokaoskdopaskdp", False],
    ["1234567890987654321", False],
    ["1234567890", False],
    [str(bson.objectid.ObjectId()), True]
]


@p("value, expected", scenarios)
def test_is_an_objectid_valis(value, expected):
    """TODO: Docstring for test_is_valis.

    :arg1: TODO
    :returns: TODO

    """
    result = utils.is_a_valid_objectid(value)

    assert result is expected
