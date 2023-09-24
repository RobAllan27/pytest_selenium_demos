import pytest


@pytest.mark.maths
def add_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.

    :param num1: The first number.
    :param num2: The second number.
    :return: The sum of num1 and num2.
    """
    result = num1 + num2
    return result


@pytest.mark.maths
def test_small_numbers():

    assert add_numbers(1, 2) == 3, "Sum of 1 and 2 should be 3"


@pytest.mark.maths
def test_large_numbers():
    assert add_numbers(10, 240) == 340, "Sum of 100 and 240 should be 340"


@pytest.mark.math
def test_large_numbers_again():
    assert add_numbers(100, 240) == 340, "Sum of 100 and 241 should be 341"
