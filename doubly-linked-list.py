# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLL(object):
    def __init__(self, vals):
        self.head = None
        self.tail = None

        # if pass iterable

    def insert(self, val):
        """Insert the value 'val' at the head of the list"""
        new = Node(val)
        if self.head is None:
            self.head, self.tail = new
        else:
            tmp = self.head
            

    def append(self, val):
        """Append the value 'val' at the tail of the list"""
        pass

    def pop(self):
        pass

    def shift(self):
        pass

    def remove(self, val):
        pass