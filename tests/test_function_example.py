import pytest
from src.function_example import show_error
        
def test_show_error_raises_zero_division_error():
    # Act
    with pytest.raises(ZeroDivisionError) as exc_info:
        show_error()

    # Assert
    assert "division by zero" in str(exc_info.value)
        
