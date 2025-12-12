from src.errors import NegativeValueError


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Сортировка по разрядам
    :param a: массив чисел
    :param base: система счисления для расчета
    :return: отсортированный массив
    """
    r_mx = max([len(str(i)) for i in a])

    bins = [[] for _ in range(base)]

    for i in range(r_mx):

        for x in a:
            if x < 0:
                raise NegativeValueError(radix_sort)
            dig = (x // base ** i) % base
            bins[dig].append(x)
        a = [x for i in bins for x in i]
        bins = [[] for _ in range(base)]
    return a






