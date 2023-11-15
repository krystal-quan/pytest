import pytest

@pytest.mark.parametrize("value",range(10))
def test_multi_param(value):
    assert 0 == value