import pytest
from src.shapes.rectangle import Rectangle

# Happy path tests with various realistic test values
@pytest.mark.parametrize("length, width, expected_area, expected_perimeter, test_id", [
    (4, 2, 8, 12, 'area_perimeter_positive_integers'),
    (5.5, 3.3, 18.15, 17.6, 'area_perimeter_floats'),
    (1, 1, 1, 4, 'area_perimeter_squares'),
    (0, 0, 0, 0, 'area_perimeter_zero_values'),
], ids=lambda test_id: test_id)
def test_rectangle_area_and_perimeter(length, width, expected_area, expected_perimeter, test_id):
    # Act
    rectangle = Rectangle(length, width)
    calculated_area = rectangle.area()
    calculated_perimeter = rectangle.perimeter()

    # Assert
    assert calculated_area == expected_area, f"Test failed for {test_id} on area"
    assert calculated_perimeter == expected_perimeter, f"Test failed for {test_id} on perimeter"

# Edge cases
@pytest.mark.parametrize("length, width, test_id", [
    (-1, 5, 'negative_length'),
    (5, -1, 'negative_width'),
    (-1, -1, 'negative_length_and_width'),
], ids=lambda test_id: test_id)
def test_rectangle_with_negative_values(length, width, test_id):
    # Act
    with pytest.raises(ValueError) as excinfo:
        rectangle = Rectangle(length, width)

    # Assert
    assert "Length and width must be positive" in str(excinfo.value), f"Test failed for {test_id}"

# Error cases
@pytest.mark.parametrize("length, width, test_id", [
    ('a', 5, 'non_numeric_length'),
    (5, 'b', 'non_numeric_width'),
    ('a', 'b', 'non_numeric_length_and_width'),
], ids=lambda test_id: test_id)
def test_rectangle_with_non_numeric_values(length, width, test_id):
    # Act
    with pytest.raises(TypeError) as excinfo:
        rectangle = Rectangle(length, width)

    # Assert
    assert "Length and width must be numeric" in str(excinfo.value), f"Test failed for {test_id}"
