from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        """ Проверка передаваемой Node"""
        if not isinstance(node, (type(None), self.__class__)):
            raise TypeError

    @property
    def next(self):
        """Возвращает ссылку на сл.узел"""
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        """Устанавливает ссылку на сл. узел"""
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["DoubleLinkedNode"] = None):
        """
        Инициализация нового узла двусвязного списка
        :param value: значение в узле
        :param next_: предыдущий узел
        :param prev: следующий узел
        """
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        prev_node = "None" if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_node = "None" if self.next is None else f"DoubleLinkedNode({self.next})"
        return f"DoubleLinkedNode({self.value}, {prev_node}, {next_node})"

    @property
    def prev(self):
        """ Возврат ссылки на предыдущий узел"""
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        """ установка значения предыдущего узла"""
        self.is_valid(prev)
        self._prev = prev


