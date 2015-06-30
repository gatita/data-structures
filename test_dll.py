# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from dll import DLL


@pytest.fixture()
def make_list():
    return DLL([1, 2, 3])


# create linked list, == empty list
def test_create_list_empty():
    mylist = DLL()
    assert mylist.head is None


# create linked list, when passed iterable
def test_create_list(make_list):
    assert make_list.size() == 3
    assert make_list.head.value == 3


# insert to empty list
def test_insert_node_empty():
    mylist = DLL()
    mylist.insert(1)
    assert mylist.size() == 1
    assert mylist.head.value == 1


# insert to populated list
def test_insert_node():
    mylist = DLL([1, 2, 3])
    mylist.insert(1)
    assert mylist.size() == 4
    assert mylist.head.value == 1
    mylist.insert(2)
    assert mylist.size() == 5
    assert mylist.head.value == 2


# pop from empty list
def test_pop_empty():
    my_list = DLL()
    with pytest.raises(IndexError):
        my_list.pop()


# pop from populated list
def test_pop():
    mylist = DLL([1, 2, 3])
    mylist.pop()
    assert mylist.size() == 2
    assert mylist.head.value == 2


# test size on empty linked list
def test_size_empty():
    mylist = DLL()
    assert mylist.size() == 0


# test size function
def test_size():
    my_list = DLL([1, 2, 3])
    assert my_list.size() == 3


# add elements, search for non-existent val
def test_search_fake():
    mylist = DLL([1, 2, 3])
    assert mylist.search(4) is None


# search for real val
def test_search():
    mylist = DLL([1, 2, 3])
    assert mylist.search(3).value == 3


def test_remove_last():
    mylist = DLL([1, 2, 3])
    mylist.remove(mylist.search(1))
    assert mylist.head.next.next is None


# remove element
def test_remove_first():
    mylist = DLL([1, 2, 3])
    mylist.remove(mylist.search(3))
    assert mylist.head.value == 2


def test_remove_middle():
    mylist = DLL([1, 2, 3])
    mylist.remove(mylist.search(2))
    assert mylist.head.next.value == 1


def test_display():
    mylist = DLL([1, 2, 3])
    assert mylist.display() == '(3, 2, 1)'
