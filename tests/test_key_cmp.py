import pytest

from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.quick_sort import quick_sort


def test_keys_in_sorts():
    array1 = [0, 5, 10, 7]
    key1 = lambda x: -x
    array2 = ['Moscow', "New York", "Tokyo", "Sankt-Petersburg"]
    key2 = lambda x : len(x)
    array3 = [(3, 0), (100, 1000), (45, 23), (1, -5)]
    key3 = lambda x: x[1]
    assert quick_sort(array1, key=key1) == [10, 7, 5, 0]
    assert bubble_sort(array2, key=key2) == ['Tokyo', 'Moscow', 'New York', 'Sankt-Petersburg']
    assert heap_sort(array3, key=key3) == [(1, -5), (3, 0), (45, 23), (100, 1000)]



def compare_desc(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0



def compare_len_desc(a, b):
    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        return 0


def compare_second_elem_asc(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0


def test_cmp_in_sorts():
    array1 = [0, 5, 10, 7]
    cmp1 = compare_desc
    array2 = ['Moscow', "New York", "Tokyo", "Sankt-Petersburg"]
    cmp2 = compare_len_desc
    array3 = [(3, 0), (100, 1000), (45, 23), (1, -5)]
    cmp3 = compare_second_elem_asc
    assert quick_sort(array1, cmp=cmp1) == [10, 7, 5, 0]
    assert bubble_sort(array2, cmp=cmp2) == ['Sankt-Petersburg', 'New York', 'Moscow', 'Tokyo']
    assert heap_sort(array3, cmp=cmp3) == [(1, -5), (3, 0), (45, 23), (100, 1000)]