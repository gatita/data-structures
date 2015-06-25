# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import linked_list as ll

class Stack(object):

    def __init__(self, values):
        # stack has-a linked list
        self.container = ll.LinkedList()

        if values:
            self.container = ll.LinkedList(values)

    def push(self, value):
        self.container.insert(value)

    def pop(self):
        self.container.pop()

    def __repr__(self):
        self.container.display()

if __name__ == '__main__':
    mystack = Stack([1, 2, 3])
    print(mystack.container.display())
    mystack.pop()
    mystack.push(9)
    mystack.push(8)
    print(mystack.container.display())

