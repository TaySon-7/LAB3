from src.errors import GeneratorError
import random


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Генерирует массив со случайными вещественными числами из диапазона lo:hi
    :param n: длина массива
    :param lo: нижняя граница генерации
    :param hi: верхняя граница генерации
    :param seed: генерационный параметр
    :return: массив из чисел
    """
    if lo > hi:
        raise GeneratorError("Начальная граница не может быть больше верхней")
    if n < 0:
        raise GeneratorError("размер массива не может быть отрицательным")
    if seed:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]