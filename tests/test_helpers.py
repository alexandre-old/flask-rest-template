import pytest
from passlib.hash import sha256_crypt, sha512_crypt
from app import helpers


get_hash_algorithm_scenarios = [
    ['SHA256', sha256_crypt],
    ['SHA512', sha512_crypt],
]

get_hash_algorithm_error_scenarios = [
    [12345, 'The parameter "hash_algorithm" should be a string.'],
    ['INVALID NAME', 'Invalid hash method.'],
]


@pytest.mark.parametrize(
    'hash_algorithm, expected', get_hash_algorithm_scenarios)
def test_get_hash_algorithm(hash_algorithm, expected):
    assert helpers.get_hash_algorithm(hash_algorithm) == expected


@pytest.mark.parametrize(
    'value, expected', get_hash_algorithm_error_scenarios)
def test_get_hash_algorithm_invalid_hash_alg(value, expected):
    with pytest.raises(ValueError) as error:
        helpers.get_hash_algorithm(value)

    assert str(error.value) == expected


def test_encrypt_password(app):
    hash = helpers.encrypt_password('password')

    # hash 256 or 512, yep, a little bit hard code for now
    assert 75 <= len(hash) <= 120


def test_verify_password():

    hash = helpers.encrypt_password("password")
    assert helpers.verify_password("password", hash) is True
    assert helpers.verify_password("invalid", hash) is False


def test_standardize_api_response_invalid_result_key(result, expected):
    with pytest.raises(ValueError) as error:
        helpers.standardize_api_response(result)
    assert error.message == expected
