def counting_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчётом
    :param a: массив для сортировки
    :return: отсоритрованный массив
    """
    mx, mn = max(a), min(a)
    cnt = [0] * (mx - mn + 1)
    res = []
    for i in a:
        cnt[i - mn] += 1
    for i in range(0, mx - mn + 1):
        for j in range(cnt[i]):
            res.append(i + mn)
    return res
