# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = None
        self.prev = None


class DLL(object):
    """ """

    def __init__(self, vals=None):
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
        tmp = self.head
        if not self.head:
            raise IndexError
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return tmp.val

    def shift(self):
        if not self.head:
            raise IndexError
        else:
            tmp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return tmp.val

    def remove(self, val):
        current = self.head
        # find the node
        while True:
            if current.val == val:
                break
            else:
                current = current.next
        # check if head node
        if current == self.head:
            self.head.next.prev = None
            self.head = self.head.next
        # check if tail node
        elif current == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

