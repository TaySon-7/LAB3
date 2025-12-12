import pytest
from src.structures.stack import Stack
from src.errors import EmptyError


def test_stack():
    s = Stack([1, 2, 4])
    assert s.head.data == 4
    s.push(100)
    assert len(s) == 4
    assert s.pop() == 100
    assert len(s) == 3
    assert s.peek() == 4


def test_queue_errors_1():
    with pytest.raises(EmptyError):
        s = Stack()
        s.pop()


def test_queue_errors_2():
    with pytest.raises(EmptyError):
        s = Stack()
        s.peek()