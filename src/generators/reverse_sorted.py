from src.errors import GeneratorError


def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует отсортированный в обратном порядке массив
    :param n: размер массива
    :return: массив чисел
    """
    if n < 0:
        raise GeneratorError("размер массива не может быть отрицательным")
    return [x for x in range(n - 1, -1, -1)]