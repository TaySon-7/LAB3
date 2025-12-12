from src.structures.node import Node
from src.errors import EmptyError


class Queue:

    def __init__(self, lst=None):
        self.head = None
        self.size = 0
        self.tail = None

        if lst:
            for i in lst:
                self.enqueue(i)

    def enqueue(self, x: int) -> None:
        """
        Добавление элемента в очередь
        :param x: элемент
        :return:
        """
        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> int:
        """
        Удаляет элемент из очереди
        :return: удаленный элемент
        """
        if self.size > 0:
            elem = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            self.size -= 1
            return elem
        raise EmptyError()

    def front(self) -> int:
        """
        Возвращает первый эелемент очереди
        :return: элемент
        """
        if self.size > 0:
            return self.head.data
        raise EmptyError

    def is_empty(self) -> int:
        """
        Показывает пустая ли очередь
        :return: True/False в зависимости от очереди
        """
        if self.size == 0:
            return True
        return False

    def __len__(self) -> int:
        """
        Показывает длину очереди
        :return: возвращает число элементов в очереди
        """
        return self.size
