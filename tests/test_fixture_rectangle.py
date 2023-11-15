import pytest
from src.shapes.rectangle import Rectangle

@pytest.fixture(autouse=True)
def setup_teardown():
    # This function will be called before each test function
    print("\nSetup before each test")
    
    yield
    # This code will be executed after each test function
    print("\nTeardown after each test")
@pytest.fixture
def setup():
    return Rectangle(4, 2)

def test_case1(setup):
    assert setup.area() == 8, "Test failed on area"

def test_case2(setup):
    assert setup.perimeter() == 12, "Test failed on perimeter"
