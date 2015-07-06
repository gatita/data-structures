# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import binheap


class Node(object):
    """Node for use in a Priority Queue."""

    def __init__(self, val, priority):
        """Create a Node with a val and a priority."""
        self.val = val
        self.priority = priority

    def __eq__(self, other):
        """Redefining equality to compare Nodes by priority."""
        return self.priority == other.priority

    def __lt__(self, other):
        """Redefining less-than to compare Nodes by priority."""
        return self.priority < other.priority

    def __gt__(self, other):
        """Redefining greater-than to compare Nodes by priority."""
        return self.priority > other.priority

    def __repr__(self):
        return ('(val:' + repr(self.val) +
                ' pri:' + repr(self.priority) + ')')


class PriorityQueue(object):
    def __init__(self, vals=None):
        """Create an empty Priority Queue.

        Priority Queue is implemented as a Binary Heap (min heap). So
        higher priority is given to Nodes with a lower priority value.

        Args:
            vals: an optional iterable of Nodes to be inserted into the
            Priority Queue when it is created. The Nodes should be
            Priority Queue Nodes and contain a priority attribute.
        """
        self.container = binheap.BinaryHeap(vals)

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return repr(self.container.heap)

    def insert(self, val, priority):
        """Insert a val and associated priority into the Priority Queue.

        The val and priority pair will be used to create a new node,
        which will then be inserted into the Priority Queue.
        """
        new = Node(val, priority)
        self.container.heap.append(new)
        i = len(self.container) - 1
        self.container._perc_up(i)

    def pop(self):
        """Remove the highest priority Node from the queue."""
        self.container.pop()

    def peek(self):
        """Return the Node with the highest priority.

        Does not remove the Node from the Priority Queue.
        """
        return self.container.heap[0]
