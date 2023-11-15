import pytest
from src.shapes.rectangle import Rectangle

class TestCircle:
    def setup_method(self):
        self.rectangle = Rectangle(4, 2)
        
    def teardown_method(self):
        self.rectangle = None
        
    def test_rectangle_area(self):
        # Act
        calculated_area = self.rectangle.area()
        
        # Assert
        assert calculated_area == self.rectangle.width * self.rectangle.length, "Test failed on area"
        
    def test_rectangle_perimeter(self):
        # Act
        calculated_perimeter = self.rectangle.perimeter()
        
        # Assert
        assert calculated_perimeter == 2 * (self.rectangle.width + self.rectangle.length), "Test failed on perimeter"
        
    def test_rectangle_with_negative_values(self):
        # Act
        with pytest.raises(ValueError) as excinfo:
            rectangle = Rectangle(-1, 5)
            
        # Assert
        assert "Length and width must be positive" in str(excinfo.value), "Test failed on negative values"
        
    def test_rectangle_with_non_numeric_values(self):
        # Act
        with pytest.raises(TypeError) as excinfo:
            rectangle = Rectangle('a', 5)
            
        # Assert
        assert "Length and width must be numeric" in str(excinfo.value), "Test failed on non-numeric values"
        
    def test_rectangle_with_zero_values(self):
        # Act
        rectangle = Rectangle(0, 0)
        
        # Assert
        assert rectangle.area() == 0, "Test failed on zero values"
        assert rectangle.perimeter() == 0, "Test failed on zero values"
        
    def test_rectangle_with_float_values(self):
        # Act
        rectangle = Rectangle(5.5, 3.3)
        
        # Assert
        assert rectangle.area() == 18.15, "Test failed on float values"
        assert rectangle.perimeter() == 17.6, "Test failed on float values"
        
    