from typing import Callable
from timeit import timeit
from copy import deepcopy
from src.constants import SORTS
from src.generators.nearly_sorted import nearly_sorted
from src.generators.reverse_sorted import reverse_sorted
from src.generators.many_duplicates import many_duplicates
from src.generators.rand_int_array import rand_int_array
from src.generators.rand_float_array import rand_float_array



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
        res[sort_name]["mid"] = 0
        for array_name, array in arrays.items():
            try:
                time_test = timeit(sort_func, deepcopy(array))
                res[sort_name][array_name] = time_test
                res[sort_name]["mid"] += time_test
            except Exception:
                res[sort_name][array_name] = -33
    for key in res.keys():
        res[key]["mid"] /= 5
    return res


def packet_arrays(n: int) -> dict[str, list]:
    dt = {}
    array1 = rand_int_array(n, 1, 1000)
    dt["int"] = array1
    array2 = rand_float_array(n, 1, 1000)
    dt["float"] = array2
    array3 = many_duplicates(n)
    dt["duplicates"] = array3
    array4 = reverse_sorted(n)
    dt["reverse"] = array4
    array5 = nearly_sorted(n, 5)
    dt["nearly"] = array5
    return dt


array = packet_arrays(10000)
b = sorting_benchmarks(SORTS, array)
print(b)


