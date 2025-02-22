import math
import pytest
from src.area import calculate_area_square

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square("2")

def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([2])

def test_calculate_area_square_accuracy():
    # For student ID 100940517, the last two digits are 17.
    # To get an output of 17, use sqrt(17) because (sqrt(17))^2 = 17.
    value = math.sqrt(17)
    assert calculate_area_square(value) == pytest.approx(17)

def test_calculate_area_square_failure():
    # Intentional error: the expected value is set incorrectly.
    # For example, asserting 5^2 equals 24 instead of 25.
    assert calculate_area_square(5) == 24
