# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import linked_list as ll


class Queue(object):
    """Container to hold nodes in a first in first out order.

    Implemented enqueue(val), dequeue(), and size()"""

    def __init__(self):
        """Initialize a new empty queue.
        The queue has a linked list as its container.
        """

        self.container = ll.LinkedList()
        self.tail = self.container.head

    def enqueue(self, val):
        """Add a node to the end of the queue whose value is val."""

        new_node = ll.Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.container.head = new_node

    def dequeue(self):
        """Remove the first node from the queue and return its value."""

        node_val = self.container.pop()

        # reset head and tail if queue becomes empty
        if len(self.container) == 0:
            self.container.head = None
            self.tail = self.container.head

        return node_val

    def size(self):
        """Return the size of the queue.
        Should return 0 if empty
        """
        return len(self.container)
