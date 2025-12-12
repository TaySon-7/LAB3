from src.errors import GeneratorError
import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed=None) -> list[int]:
    """
    Генерирует массив со случайными целыми числами из диапазона lo:hi
    :param n: длина массива
    :param lo: нижняя граница генерации
    :param hi: верхняя граница генерации
    :param distinct: True, если все числа должны быть различны
    :param seed: генерационный параметр
    :return: массив из чисел
    """
    if lo > hi:
        raise GeneratorError("Начальная граница не может быть больше верхней")
    if n < 0:
        raise GeneratorError("размер массива не может быть отрицательным")
    if distinct > hi - lo + 1:
        raise GeneratorError(f"с такми границами невозможно сгенерировать {distinct} случайных значений")
    if seed:
        random.seed(seed)
    if distinct:
        return random.sample(range(lo, hi + 1), n)
    return [random.randint(lo, hi) for _ in range(n)]