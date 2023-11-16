import pytest
# Pytest example
# @pytest.mark.xfail
@pytest.mark.parametrize("value",range(10000))
def test_time_pytest(value):
    assert value == value