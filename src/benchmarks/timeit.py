import time


def timeit(func, *args, **kwargs) -> float:
    """
    Подсчет времени выполенеия функции
    :param func: вид функции
    :param args: позиционные аргументы
    :param kwargs: именованные аргументы
    :return: время выполнения функции
    """
    begin = time.perf_counter()
    func(*args, **kwargs)
    stop = time.perf_counter()
    return stop - begin
