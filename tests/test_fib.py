import pytest
from src.algorithms.fibo import fibo_iter, fibo_recursive
from src.errors import NegativeValueError


def test_fib():
    assert fibo_iter(0) == fibo_recursive(0) == 0
    assert fibo_iter(5) == fibo_recursive(5) == 5
    assert fibo_iter(7) == fibo_recursive(7) == 13
    assert fibo_iter(10) == fibo_recursive(10) == 55


def test_fib_iter_negative():
    with pytest.raises(NegativeValueError):
        assert fibo_iter(-1)


def test_fib_rec_negative():
    with pytest.raises(NegativeValueError):
        assert fibo_recursive(-1)
