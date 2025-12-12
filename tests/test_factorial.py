import pytest
from src.algorithms.factorial import factorial_iter, factorial_recursive
from src.errors import NegativeValueError


def test_fact():
    assert factorial_iter(0) == factorial_recursive(0) == 1
    assert factorial_iter(5) == factorial_recursive(5) == 120
    assert factorial_iter(7) == factorial_recursive(7) == 5040
    assert factorial_iter(10) == factorial_recursive(10) == 3628800


def test_fib_iter_negative():
    with pytest.raises(NegativeValueError):
        assert factorial_iter(-1)


def test_fib_rec_negative():
    with pytest.raises(NegativeValueError):
        assert factorial_recursive(-1)
