import pytest
from bson.objectid import ObjectId

from app import utils

object_id_scenarios = [
    [ObjectId(), True],
    [str(ObjectId()), True],
    ['invalid', False],
    ['11002299338844775566', False],
    [1234567890, False],
    [[], False]
]


@pytest.mark.parametrize('value, expected', object_id_scenarios)
def test_is_a_valid_object_id(value, expected):
    utils.is_a_valid_object_id(value) is expected
