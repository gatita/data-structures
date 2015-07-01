# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, _next=None, _prev=None):
        self.val = val
        self.next = _next
        self.prev = _prev


class DLL(object):
    """Container to hold nodes with pointers to a node's previous and
    next node
    """

    def __init__(self, vals=None):
        """Create an empty doubly-linked-list or optionally pass in an
        iterable to create a populated doubly-linked-list
        """

        self.head = None
        self.tail = None

        if vals:
            for v in vals:
                self.insert(v)

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
        if self.tail is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def pop(self):
        """Remove the value at the head of the list and return its
        value"""

        tmp = self.head
        if self.head is None:
            raise IndexError
        elif self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return tmp.val

    def shift(self):
        """Remove the value at the tail of the list and return its
        value"""

        tmp = self.tail
        if self.head is None:
            raise IndexError
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return tmp.val

    def remove(self, val):
        """Remove a node whose value is 'val'"""

        current = self.head

        # find the node
        while True:
            if current is None:
                raise IndexError('val not in list')
            elif current.val == val:
                break
            else:
                current = current.next

        if self.head is self.tail:
            self.head = self.tail = None
        elif current is self.head:
            self.head.next.prev = None
            self.head = self.head.next
        elif current is self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
