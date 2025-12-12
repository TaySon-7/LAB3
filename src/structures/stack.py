from src.structures.node import Node
from src.errors import EmptyError

class Stack:
    """
    Структура стека
    """
    def __init__(self, lst=None):
        self.size = 0
        self.head = None
        if lst:
            for i in lst:
                self.push(i)

    def pop(self) -> int:
        """
        Удаление последнего элемента стека
        :return: удаленный элемент
        """
        if self.size > 0:
            elem = self.head.data
            self.size -= 1
            self.head = self.head.next
            return elem

        raise EmptyError()

    def push(self, x: int) -> None:
        """
        Добавление эелемента в стек
        :param x: элемент
        :return:
        """
        node = Node(x)
        if self.head is None:
            cur_mn = x
        else:
            node.next = self.head
            cur_mn = min(x, self.head.cur_mn)
        self.size += 1
        node.cur_mn = cur_mn
        self.head = node

    def is_empty(self) -> bool:
        """
        Проверка на пустоту
        :return: True/False в зависимости от стека
        """
        if self.size == 0:
            return True
        return False

    def peek(self) -> int:
        """
        Выдает последний элемпент стека
        :return: Последний элемент стека
        """
        if self.size > 0:
            return self.head.data
        raise EmptyError()

    def min(self) -> int:
        """Возвращает минимальный элемпент стека сложность О(1)
        :return: минимальный элемент
        """
        if self.size > 0:
            return self.head.cur_mn
        raise EmptyError()

    def __len__(self):
        """
        Показывает текущую длину стека
        :return: число длины
        """
        return self.size
