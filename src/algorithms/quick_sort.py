from random import randint
from typing import Callable, Any, TypeVar
from functools import cmp_to_key
T = TypeVar('T')


def quick_sort(a: list[T], key: Callable[[T], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Быстрая сортировка
    :param a: массив чисел
    :param key: ключ определяющий сравнение
    :param cmp: компаратор
    :return: отсортированный массив
    """
    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x
    ln = len(a)
    if ln <= 1:
        return a
    pivot = a[randint(0, ln - 1)]
    left = [x for x in a if key(x) < key(pivot)]
    mid = [x for x in a if key(x) == key(pivot)]
    right = [x for x in a if key(x) > key(pivot)]
    return quick_sort(left, key) + mid + quick_sort(right, key)


