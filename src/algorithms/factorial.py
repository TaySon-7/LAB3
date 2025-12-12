from src.errors import NegativeValueError

def factorial_iter(n: int) -> int:
    """
    Итеративное вычисление факторила
    :param n: число для вычисления факториала:
    :return: n!
    """
    if n < 0:
        raise NegativeValueError(factorial_iter)
    res = 1
    for i in range(2, (n + 1)):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    """
    Рекурсивное вычисление факториала
    :param n: число для вычисления факториала
    :return: n!
    """
    res = n
    if n < 0:
        raise NegativeValueError(factorial_recursive)
    elif n == 0:
        return 1
    return res * factorial_recursive(n - 1)



