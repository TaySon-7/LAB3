from src.algorithms.quick_sort import quick_sort


def bucket_sort(a: list[float], buckets: int | None=None) -> list[float]:
    """
    Вёдерная сортировка
    :param a: массив чисел
    :param buckets: число корзин
    :return: отсортированный массив
    """
    if buckets is None:
        n = len(a)
        buckets = [[] for _ in range(n)]
    else:
        n = buckets
        buckets = [[] for _ in range(n)]
    for num in a:
        bucket_idx = int(num * n)
        buckets[bucket_idx].append(num)

    for i in range(len(buckets)):
        bucket = quick_sort(buckets[i])
        buckets[i] = bucket

    ans = [x for bucket in buckets for x in bucket]
    return ans
