# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None

        # if iterable supplied, add all elements
        if values:
            for v in values:
                self.insert(v)

    def insert(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        # check to see if list is empty
        if not self.head:
            raise IndexError

        # add head to tmp val
        tmp = self.head
        # make new head old head's next
        self.head = self.head.next
        return tmp.value

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, val):
        current = self.head
        while current:
            if current.value == val:
                break
            current = current.next
        return current

    def remove(self, node):
        ''' InteractivePython.org helped with this function. '''
        current = self.head
        previous = None

        # find node, get pointers in right places
        while True:
            if current == node:
                break
            else:
                previous = current
                current = current.next

        # check if head node
        if self.head == node:
            self.head = current.next
        # not head node
        else:
            previous.next = current.next
            current.next = None

    def display(self):
        current = self.head
        if current:
            output = "("
            while current.next:
                output += str(current.value) + ', '
                current = current.next
            output += str(current.value) + ')'
            return output
        else:
            return "()"

    def __repr__(self):
        return self.display()


if __name__ == '__main__':
    mylist = LinkedList()
    print(mylist)
    mylist.insert(3)
    mylist.insert(2)
    mylist.insert(6)
    print(mylist.display())
    print("list size: " + str(mylist.size()))
    mynode = mylist.search(6)
    print(str(mynode.value))
    print(mynode)
    mylist.remove(mynode)
    print(mylist.display())
    newlist = LinkedList([1, 2, 3])
    print(newlist.display())
