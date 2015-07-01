# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function


class BinaryHeap(object):

    def __init__(self, values=None):
        """Create an empty Binary Heap or optionally create one
        populated with values
        """

        self.heap = []

        if values is not None:
            for v in values:
                self.push(v)

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        self._perc_up(i)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError

        self.heap[0] = self.heap[len(self.heap)-1]
        self._perc_down()

    def _perc_up(self, i):
        while (i+1) / 2 > 0:
            if self.heap[i] < self.heap[i / 2]:
                self.heap[i], self.heap[i / 2] = self.heap[i / 2], self.heap[i]
            i = (i) / 2

    def _perc_down(self, i=0):
        size = len(self.heap) - 1
        while i * 2 <= size:
            if self.heap[i] > self.heap[i * 2 + 1]:
                self.heap[i], self.heap[i*2+1] =\
                    self.heap[i*2+1], self.heap[i]
                i = i * 2 + 1

            elif self.heap[i] > self.heap[(i+1) * 2]:
                self.heap[i], self.heap[(i+1) * 2] =\
                    self.heap[(i+1) * 2], self.heap[i]
                i = (i+1) * 2

    def __len__(self):
        return len(self.heap)
