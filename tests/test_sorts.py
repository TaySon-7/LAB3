import pytest
from src.generators.nearly_sorted import nearly_sorted
from src.generators.reverse_sorted import reverse_sorted
from src.generators.many_duplicates import many_duplicates
from src.generators.rand_int_array import rand_int_array
from src.generators.rand_float_array import rand_float_array
from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.radix_sort import radix_sort
from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.counting_sort import counting_sort
from src.algorithms.quick_sort import quick_sort
import random


def test_int_rand_sorting():
    n = random.randint(1, 1000)
    array = rand_int_array(n, 1, 1000)
    assert quick_sort(array) == sorted(array)
    assert bubble_sort(array) == sorted(array)
    assert radix_sort(array) == sorted(array)
    assert heap_sort(array) == sorted(array)
    assert counting_sort(array) == sorted(array)


def test_float_rand_sorting():
    n = random.randint(1, 1000)
    array = rand_float_array(n, 1, 1000)
    assert quick_sort(array) == sorted(array)
    assert bubble_sort(array) == sorted(array)
    assert heap_sort(array) == sorted(array)


def test_float_bucket_sorting():
    n = random.randint(1, 1000)
    array = rand_float_array(n, 0.0, 1.0)
    assert bucket_sort(array) == sorted(array)


def test_nearly_sorting():
    n = random.randint(1, 1000)
    sw = random.randint(1, n)
    array = nearly_sorted(n, sw)
    assert quick_sort(array) == sorted(array)
    assert bubble_sort(array) == sorted(array)
    assert radix_sort(array) == sorted(array)
    assert heap_sort(array) == sorted(array)
    assert counting_sort(array) == sorted(array)


def test_reverse_sorting():
    n = random.randint(1, 1000)
    array = reverse_sorted(n)
    assert quick_sort(array) == sorted(array)
    assert bubble_sort(array) == sorted(array)
    assert radix_sort(array) == sorted(array)
    assert heap_sort(array) == sorted(array)
    assert counting_sort(array) == sorted(array)


def test_duplicates_sorting():
    n = random.randint(1, 1000)
    array = many_duplicates(n)
    assert quick_sort(array) == sorted(array)
    assert bubble_sort(array) == sorted(array)
    assert radix_sort(array) == sorted(array)
    assert heap_sort(array) == sorted(array)
    assert counting_sort(array) == sorted(array)
