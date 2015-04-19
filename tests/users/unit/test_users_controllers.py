import pytest
from app.users import controllers


is_an_available_username_scenarios = [
    ['username-foo', True],
    ['username-bar', False]
]


@pytest.mark.parametrize(
    'username, expected', is_an_available_username_scenarios)
def test_is_an_available_username(username, expected):
    assert controllers.is_an_available_username(username) is expected
