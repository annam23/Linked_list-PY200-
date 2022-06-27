from typing import Any, Optional, Iterable
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        node.value = value

    def __len__(self) -> int:
        """ Возвращает длину связного списка """
        return self._len

    def _check_indexes(self, index: int):
        """ Функция для проверки соответствия индекса"""
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:
            raise IndexError()

    def __delitem__(self, index: int) -> Any:
        """ Метод удаляет узел по заданному индексу"""

        self._check_indexes(index)

        self._len -= 1

        if index == 1:
            del_node = self._head
            self._head = self._step_by_step_on_nodes(index + 1)
            del del_node

        else:
            del_node = self._step_by_step_on_nodes(index)
            bef_node = self._step_by_step_on_nodes(index - 1)
            bef_node.next = del_node.next
            del del_node

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def insert(self, index, value):
        """ Добавление элемента в связанный список по указанному индексу"""
        self._check_indexes(index)

        insert_node = Node(value)

        self._len += 1
        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        self._len += 1
        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

    def _step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        self._check_indexes(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self.__setitem__(self._len, value)

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self.__setitem__(1, value)


class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    @staticmethod
    def dbl_linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


