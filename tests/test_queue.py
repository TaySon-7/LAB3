import pytest
from src.structures.queue import Queue
from src.errors import EmptyError


def test_queue():
    q = Queue([1, 2, 4])
    assert q.head.data == 1
    assert q.tail.data == 4
    q.enqueue(100)
    assert len(q) == 4
    assert q.dequeue() == 1
    assert len(q) == 3
    assert q.front() == 2


def test_queue_errors_1():
    with pytest.raises(EmptyError):
        q = Queue()
        q.dequeue()


def test_queue_errors_2():
    with pytest.raises(EmptyError):
        q = Queue()
        q.front()