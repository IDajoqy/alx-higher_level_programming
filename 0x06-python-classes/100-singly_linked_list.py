#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, date, next_node=None):
        """Initialize a new Node.

        Args:
           data (int): the data of the new node.
           next_node (Node): the next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a node object")
        self.__next_node = value

    class singlylinkedlist:
        """Represent a singly-linked list."""

        def __init__(self):
            """Initialize a new singlylinkedlist."""
            self.__head - None
