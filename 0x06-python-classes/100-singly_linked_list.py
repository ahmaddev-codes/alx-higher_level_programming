#!/usr/bin/python3
"""
A module that contains a singly linked list
"""


class Node:
    """defines the node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.__head

        while current is not None:
            if current.next_node is None:
                result += str(current.data)
            else:
                result += str(current.data) + "\n"

            current = current.next_node

        return result
