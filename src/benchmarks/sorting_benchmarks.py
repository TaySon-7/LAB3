from copy import deepcopy
from typing import Callable
from timeit import timeit
from copy import deepcopy


def sorting_benchmarks(sorts: dict[str, Callable], arrays: dict[str, list]) -> dict[str, dict[str, float]]:
    """
    Измеряет время работы сортировок на конкретных массивах
    :param sorts: виды сортировок
    :param arrays: различные массивы чисел для тестов
    :return: словарь с соритровками и их значениями скорости на массивах
    """
    res = {}
    for sort_name, sort_func in sorts.items():
        res[sort_name] = {}
        for array_name, array in arrays.items():
            try:
                time_test = timeit(sort_func, deepcopy(array))
                res[sort_name][array_name] = time_test
            except Exception:
                res[sort_name][array_name] = -33
    return res

print(sorting_benchmarks())
