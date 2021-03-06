# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import linked_list as ll


class Stack(object):

    def __init__(self, values=None):
        '''stack has-a linked list'''
        self.container = ll.LinkedList(values)

    def push(self, value):
        self.container.insert(value)

    def pop(self):
        return self.container.pop()


if __name__ == '__main__':
    # local tests
    my_stack = Stack()
    print(my_stack.container.display())
    mystack = Stack([1, 2, 3])
    print(mystack.container.display())
    mystack.pop()
    mystack.push(9)
    mystack.push(8)
    print(mystack.container.display())
    for i in range(6):
        print(mystack.pop())
    print(mystack.container.display())
