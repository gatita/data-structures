# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from linked_list import LinkedList


# create linked list, == empty list
# create linked list, when passed iterable
def test_create_list():
    mylist = LinkedList()
    assert mylist.head is None
    list2 = LinkedList([1, 2, 3])
    assert list2.size() == 3
    assert list2.head.value == 3


# insert to empty list
# insert to populated list
def test_insert_node():
    mylist = LinkedList()
    mylist.insert(1)
    assert mylist.size() == 1
    assert mylist.head.value == 1
    mylist.insert(2)
    assert mylist.size() == 2
    assert mylist.head.value == 2


# pop from empty list
# pop from populated list
def test_pop():
    my_list = LinkedList()
    with pytest.raises(IndexError):
        my_list.pop()

    mylist = LinkedList([1, 2, 3])
    mylist.pop()
    assert mylist.size() == 2
    assert mylist.head.value == 2


# test size function
def test_size():
    mylist = LinkedList()
    assert mylist.size() == 0
    my_list = LinkedList([1, 2, 3])
    assert my_list.size() == 3


# add elements, search for non-existent val
# search for real val
def test_search():
    mylist = LinkedList([1, 2, 3])
    assert mylist.search(4) is None
    assert mylist.search(3).value == 3


# remove element
def test_remove():
    mylist = LinkedList([1, 2, 3])
    mylist.remove(mylist.search(3))
    assert mylist.head.value == 2


# does display() return tuple
def test_display():
    mylist = LinkedList([1, 2, 3])
    assert mylist.display() == (3, 2, 1)
