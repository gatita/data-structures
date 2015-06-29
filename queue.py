# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import linked_list as ll


class Queue(object):
    def __init__(self):
        self.container = ll.LinkedList()
        self.tail = self.container.head

    def enqueue(self, val):
        new_node = ll.Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.container.head = new_node

    def dequeue(self):
        return self.container.pop()

    def size(self):
        pass

if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(7)
    print q.container.display()
