# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from linked_list import LinkedList

# create linked list, == empty list
# create linked list, when passed iterable
def test_create_list():
    newList = LinkedList()
    assert newList.head == None
    list2 = LinkedList([1, 2, 3])
    assert list2.size() == 3
    assert list2.head.value == 3

# insert to empty list
# insert to populated list
def test_insert_node():
    newList = LinkedList()
    newList.insert(1)
    assert newList.size() == 1
    assert newList.head.value == 1
    newList.insert(2)
    assert newList.size() == 2
    assert newList.head.value == 2

# pop from empty list
# pop from populated list
def test_pop():
    newList2 = LinkedList()
    assert newList2.pop() == "The list is empty."

    newList = LinkedList([1, 2, 3])
    newList.pop()
    assert newList.size() == 2
    assert newList.head.value == 2

# test size function
def test_size():
    newList = LinkedList()
    assert newList.size() == 0
    newList2 = LinkedList([1, 2, 3])
    assert newList2.size() == 3

# add elements, search for non-existent val
# search for real val
def test_search():
    newList = LinkedList([1, 2, 3])
    assert newList.search(4) == None
    assert newList.search(3).value == 3

# remove element
def test_remove():
    newList = LinkedList([1, 2, 3])
    newList.remove(newList.search(3))
    assert newList.head.value == 2


# does display() return tuple
def test_display():
    newList = LinkedList([1, 2, 3])
    assert newList.display() == (3, 2, 1)

