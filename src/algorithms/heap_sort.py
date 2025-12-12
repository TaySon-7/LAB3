from typing import Callable, Any, TypeVar
from functools import cmp_to_key
T = TypeVar('T')


def shift_down(a: list[int], n: int, i: int, key: Callable[[T], Any]):
    """
    рекурсивная перестановка потомков из корня i
    :param a: текущий массив чисел
    :param n: размер массива
    :param i: корень
    :param key: ключ определяющий сравнение
    :return: массив после перестановки
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and key(a[left]) > key(a[i]):
        i = left
    if right < n and key(a[right]) > key(a[i]):
        i = right
    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        shift_down(a, n, i, key)


def heap_sort(a: list[T], key: Callable[[T], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Пирамидальная сортировка кучи
    :param a: массив чисел
    :param key: ключ определяющий сравнение
    :param cmp: компаратор
    :return: отсортированный массив
    """
    if cmp is not None:
        key = cmp_to_key(cmp)
    if key is None:
        key = lambda x: x
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        shift_down(a, n, i, key)

    for end in range(len(a) - 1, 0, -1):
        a[end], a[0] = a[0], a[end]
        shift_down(a, end, 0, key)
    return a


