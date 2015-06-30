# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None


class DLL(object):
    def __init__(self, vals):
        self.head = None
        self.tail = None

        # if pass iterable

    def insert(self, val):
        """Insert the value 'val' at the head of the list"""
        new = Node(val)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def append(self, val):
        """Append the value 'val' at the tail of the list"""
        new = Node(val)

    def pop(self):
        pass

    def shift(self):
        pass

    def remove(self, val):
        pass