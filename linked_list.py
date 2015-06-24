# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class LinkedList(object):
    def __init__(self, values=None):
        self.head = None

    def insert(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        # check to see if list is empty
        if not self.head:
            return 'The list is empty.'
        # add head to tmp val
        tmp = self.head
        # make new head old head's next
        self.head = self.head.next
        # remove tmps link to list
        tmp.next = None
        # return tmp.value
        return tmp.value

    def size(self):
        count = 1
        if not self.head:
            return 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def search(self, val):
        pass

    def remove(self, node):
        pass

    def display(self):
        print repr(self)

    def __repr__(self):
        if not self.head:
            return 'The list is empty.'
        current = self.head
        my_list = '(' + str(current.value)
        while current.next:
            current = current.next
            my_list += ', ' + str(current.value)
        my_list += ')'
        return my_list


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
