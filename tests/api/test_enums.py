import pytest
from api.enums import is_valid_enum_domain


def test_is_valid_enum_domain():
    valid_domain_name = "asset"
    invalid_domain_name = "fake name"

    assert is_valid_enum_domain(valid_domain_name) is True
    assert is_valid_enum_domain(invalid_domain_name) is False
