from src.errors import GeneratorError
import random


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует приближенный к отсортированному массив
    :param n: размер массива
    :param swaps: количество перестановок
    :param seed: генерационный параметр
    :return: массив чисел
    """
    if n < 0:
        raise GeneratorError("размер массива не может быть отрицательным")
    if seed:
        random.seed(seed)
    a = [x for x in range(n)]
    for i in range(swaps):
         sw1, sw2 = random.sample(a, 2)
         a[sw1], a[sw2] = a[sw2], a[sw1]
    return a