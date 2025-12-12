import click
from click_shell import shell
from  constants import SORTS
from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.radix_sort import radix_sort

from src.algorithms.factorial import factorial_recursive, factorial_iter
from src.algorithms.fibo import fibo_recursive, fibo_iter
from src.structures.queue import Queue
from src.structures.stack import Stack


stack = Stack()
queue = Queue()
@shell(prompt=">3 ", intro="Алгоритмический мини-пакет")
def loop():
    pass


@loop.command("fibonacci")
@click.argument("n", nargs=1, type=int)
@click.option("-r", is_flag=True, default=False)
def cli_fibo(n: int, r: bool):
    if r:
        print(fibo_recursive(n))
    else:
        print(fibo_iter(n))


@loop.command("factorial")
@click.argument("n", nargs=1, type=int)
@click.option("-r", is_flag=True, default=False)
def cli_factorial(n: int, r: bool):
    if r:
        print(factorial_recursive(n))
    else:
        print(factorial_iter(n))


@loop.command("sort")
@click.argument("type", nargs=1, type=click.Choice(SORTS.keys()))
@click.argument("array", nargs=-1, type=int)
@click.option("--buckets", nargs=1, type=int)
def cli_sort(type: str, array, buckets: int) -> None:
    if type == "bucket_sort":
        print(*bucket_sort(array, buckets))
        return
    if type == "radix_sort":
        print(radix_sort(array))
        return
    print(SORTS[type](list(array)))


@loop.command("queue")
@click.argument("command", nargs=1, type=str)
@click.option("--item", nargs=1, type=int)
def stack_cli(command: str, item: int) -> None:
    if command == "is_empty":
        print(queue.is_empty())
    elif command == "enqueue":
        queue.enqueue(item)
    elif command == "dequeue":
        print(queue.dequeue())
    elif command == "front":
        print(queue.front())
    elif command == "len":
        print(len(queue))


@loop.command("queue")
@click.argument("command", nargs=1, type=str)
@click.option("--item", nargs=1, type=int)
def stack_cli(command: str, item: int) -> None:
    if command == "is_empty":
        print(queue.is_empty())
    elif command == "enqueue":
        queue.enqueue(item)
    elif command == "dequeue":
        print(queue.dequeue())
    elif command == "front":
        print(queue.front())
    elif command == "len":
        print(len(queue))
