import pytest
from src.shapes.square import Square

# Happy path tests with various realistic test values
@pytest.mark.parametrize("side, expected_area, expected_perimeter", [
    (1, 1, 4),  # ID: Test-Square-Area-Perimeter-1
    (2, 4, 8),  # ID: Test-Square-Area-Perimeter-2
    (10, 100, 40),  # ID: Test-Square-Area-Perimeter-10
    (0.5, 0.25, 2),  # ID: Test-Square-Area-Perimeter-0.5
])
def test_square_area_and_perimeter_happy_path(side, expected_area, expected_perimeter):
    # Act
    square = Square(side)
    area = square.area()
    perimeter = square.perimeter()

    # Assert
    assert area == expected_area, f"Expected area to be {expected_area}, but got {area}"
    assert perimeter == expected_perimeter, f"Expected perimeter to be {expected_perimeter}, but got {perimeter}"

# Edge cases
@pytest.mark.parametrize("side, expected_area, expected_perimeter", [
    (0, 0, 0),  # ID: Test-Square-Area-Perimeter-Edge-0
    (-1, 1, -4),  # ID: Test-Square-Area-Perimeter-Edge-Negative
    (1e-6, 1e-12, 4e-6),  # ID: Test-Square-Area-Perimeter-Edge-Small
    (1e6, 1e12, 4e6),  # ID: Test-Square-Area-Perimeter-Edge-Large
])
def test_square_area_and_perimeter_edge_cases(side, expected_area, expected_perimeter):
    # Act
    square = Square(side)
    area = square.area()
    perimeter = square.perimeter()

    # Assert
    assert area == expected_area, f"Expected area to be {expected_area}, but got {area}"
    assert perimeter == expected_perimeter, f"Expected perimeter to be {expected_perimeter}, but got {perimeter}"

# Error cases
@pytest.mark.parametrize("side, exception", [
    ("a", TypeError),  # ID: Test-Square-Area-Perimeter-Error-Type
    (None, TypeError),  # ID: Test-Square-Area-Perimeter-Error-None
    ([1, 2], TypeError),  # ID: Test-Square-Area-Perimeter-Error-List
])
def test_square_area_and_perimeter_error_cases(side, exception):
    # Act & Assert
    with pytest.raises(exception):
        square = Square(side)
