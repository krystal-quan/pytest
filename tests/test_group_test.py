import pytest
from src.function_example import fibonacci

class TestFibonacci:
    # Happy path tests with various realistic test values
    @pytest.mark.parametrize("test_input, expected", [
        (0, 0),  # Base case: fibonacci(0)
        (1, 1),  # Base case: fibonacci(1)
        (2, 1),  # fibonacci(2) = fibonacci(1) + fibonacci(0)
        (3, 2),  # fibonacci(3) = fibonacci(2) + fibonacci(1)
        (5, 5),  # fibonacci(5) = fibonacci(4) + fibonacci(3)
        (10, 55),  # fibonacci(10) = fibonacci(9) + fibonacci(8)
    ])
    def test_fibonacci_happy_path(self, test_input, expected):
        # Act
        result = fibonacci(test_input)

        # Assert
        assert result == expected, f"Expected fibonacci({test_input}) to be {expected}"

    # Edge cases
    @pytest.mark.parametrize("test_input, expected", [
        (0, 0),  # Edge case: fibonacci(0)
        (1, 1),  # Edge case: fibonacci(1)
    ])
    def test_fibonacci_edge_cases(self, test_input, expected):
        # Act
        result = fibonacci(test_input)

        # Assert
        assert result == expected, f"Expected fibonacci({test_input}) to be {expected}"

    # Error cases
    @pytest.mark.parametrize("test_input, exception", [
        (-1, ValueError),  # Negative input should raise ValueError
        ("a", TypeError),  # String input should raise TypeError
        (1.5, TypeError),  # Float input should raise TypeError
    ])
    def test_fibonacci_error_cases(self, test_input, exception):
        # Act / Assert
        with pytest.raises(exception):
            fibonacci(test_input)