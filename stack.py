# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import linked_list as ll


class Stack(object):

    def __init__(self, values=None):
        '''stack has-a linked list'''
        if values:
            self.container = ll.LinkedList(values)
        self.container = ll.LinkedList()

    def push(self, value):
        self.container.insert(value)

    def pop(self):
        self.container.pop()


if __name__ == '__main__':
    # local tests
    mystack = Stack([1, 2, 3])
    print(mystack.container.display())
    mystack.pop()
    mystack.push(9)
    mystack.push(8)
    print(mystack.container.display())
