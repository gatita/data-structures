# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import binheap


class Node(object):
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def __eq__(self, other):
        if self.priority == other.priority:
            return self.val == other.val
        else:
            return self.priority == other.priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.val < other.val
        else:
            return self.priority < other.priority

    def __gt__(self, other):
        if self.priority == other.priority:
            return self.val > other.val
        else:
            return self.priority > other.priority


class PriorityQueue(object):
    def __init__(self, vals=None):
        self.container = binheap.BinaryHeap()

    def insert(self, val, priority):
        new = Node(val, priority)
        self.container.heap.append(new)
        i = len(self.container) - 1
        self.container._perc_up(i)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[0]
