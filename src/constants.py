from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.radix_sort import radix_sort
from src.algorithms.counting_sort import counting_sort
from src.algorithms.bubble_sort import bubble_sort


SAMPLE_CONSTANT: int = 10

SORTS = {"bucket": bucket_sort, "quick": quick_sort, "heap": heap_sort, "radix": radix_sort,\
         "count": counting_sort, "bubble": bubble_sort}