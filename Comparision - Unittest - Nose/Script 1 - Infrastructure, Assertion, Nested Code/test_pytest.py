import pytest

def test_basic():
    assert True
    
def test_list():
    lst = [1, 3, 5, 6]
    assert [1, 3, 4] == lst


def test_string():
    assert 'pytest' == 'pyttest'