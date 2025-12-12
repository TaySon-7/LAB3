from src.errors import NegativeValueError


def fibo_iter(n: int) -> int:
    """
    Итеративное вычисление чисел Фибоначчи
    :param n: Порядковый номер числа Фибоначии
    :return: число Фибоначии на n-ой позиции
    """
    if n < 0:
        raise NegativeValueError(fibo_iter)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


def fibo_recursive(n: int, memo=None) -> int:
    """
    Рекурсивное вычисление чисел Фибоначчи
    :param n: Порядковый номер числа Фибоначии
    :param memo: словарь для хранения уже посчитанных чисел (оптимизация до O(n))
    :return: число Фибоначии на n-ой позиции
    """
    if n < 0:
        raise NegativeValueError(fibo_recursive)
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibo_recursive(n - 1, memo) + fibo_recursive(n - 2, memo)
    return memo[n]
