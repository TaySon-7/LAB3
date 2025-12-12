from copy import deepcopy
from typing import Callable, Any, TypeVar
from functools import cmp_to_key
T = TypeVar('T')

def bubble_sort(a: list[T], key: Callable[[T], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Сортировка пузырьком
    :param a: массив чисел
    :param key: ключ определяющий сравнение
    :param cmp: компаратор
    :return: отсортированный массив
    """
    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x
    res_a = deepcopy(a)
    ln = len(res_a)
    for i in range(ln - 1):
        for j in range(ln - i - 1):
            if key(res_a[j]) > key(res_a[j + 1]):
                res_a[j], res_a[j + 1] = res_a[j + 1], res_a[j]
    return res_a

