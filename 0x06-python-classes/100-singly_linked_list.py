#!/usr/bin/python3
"""Classes for singly linked list"""


class Node:
    """Node of a singly linked list
    Attributes:
        __data (int): data of node
        __next_node (None or Node Obj): next node
    """
    def __init__(self, data, next_node=None):
        """Inits a new node
        Arguments:
            data (int): data of new node
            next_node (Node): next node of new node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next node"""
        return self.__next_node

    def next_node(self, value):
        """Setter for next node"""
        if value is not None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list
    Attributes:
        __head (None or Node obj): head of linked list
    """
    def __init__(self):
        """Inits new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new node to list
        Arguments:
            value (Node): new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """How to represet a list"""
        elements = []
        temp = self.__head
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(elements))
