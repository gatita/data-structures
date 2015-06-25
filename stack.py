# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import linked_list as ll

class Stack(ll.LinkedList):

    # def __init__(self, values):
    #     # stack implemented as linked list
    #     self.stack = ll.LinkedList()

    #     if values:
    #         self.stack = ll.LinkedList(values)

    def push(self, value):
        self.insert(value)

    # def pop(self):
    #     # implemented as linked list
    #     pass

if __name__ == '__main__':
    mystack = Stack([1, 2, 3])
    print(mystack.display())
    mystack.pop()
    mystack.push(9)
    mystack.push(8)
    print(mystack.display())

