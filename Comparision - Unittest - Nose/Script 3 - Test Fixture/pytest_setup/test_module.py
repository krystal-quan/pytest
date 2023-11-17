# test_module.py
import pytest

@pytest.fixture(scope='module')
def module_fixture():
    print("\nSetting up module_fixture")
    data = {'key': 'module_value'}
    yield data
    print("\nTearing down module_fixture")

@pytest.fixture(scope='function')
def test_fixture():
    print("\nSetting up test_fixture")
    data = {'key': 'test_value'}
    yield data
    print("\nTearing down test_fixture")

def test_module_fixture_1(module_fixture):
    assert 'key' in module_fixture
    assert module_fixture['key'] == 'module_value'

def test_module_fixture_2(module_fixture):
    assert 'key' in module_fixture
    assert module_fixture['key'] == 'module_value'

def test_test_fixture_1(test_fixture):
    assert 'key' in test_fixture
    assert test_fixture['key'] == 'test_value'

def test_test_fixture_2(test_fixture):
    assert 'key' in test_fixture
    assert test_fixture['key'] == 'test_value'
