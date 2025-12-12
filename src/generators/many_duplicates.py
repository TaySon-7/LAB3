from src.errors import GeneratorError
import random

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив с определенным количеством уникальных значений
    :param n: размер массива
    :param k_unique: количество уникальных значений
    :param seed: генерационный параметр
    :return: массив чисел
    """
    if n < 0:
        raise GeneratorError("размер массива не может быть отрицательным")
    if seed:
        random.seed(seed)
    a = [x for x in range(k_unique)]
    return [random.choice(a) for _ in range(n)]