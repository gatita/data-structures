# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from dll import DLL


@pytest.fixture()
def make_list_empty():
    return DLL()


@pytest.fixture()
def make_list_one():
    return DLL([1])


@pytest.fixture()
def make_list_three():
    return DLL([1, 2, 3])


def test_create_list_empty(make_list_empty):
    assert make_list_empty.head is None
    assert make_list_empty.tail is None


def test_create_list_(make_list_three):
    assert make_list_three.head.val == 3
    assert make_list_three.head.next.val == 2
    assert make_list_three.head.next.next.val == 1
    assert make_list_three.tail.prev.prev.val == 3
    assert make_list_three.tail.prev.val == 2
    assert make_list_three.tail.val == 1


def test_insert_node_empty(make_list_empty):
    my_list = make_list_empty
    my_list.insert(1)
    assert my_list.head.val == 1
    assert my_list.tail.val == 1


def test_insert_node(make_list_three):
    my_list = make_list_three
    my_list.insert(1)
    assert my_list.head.val == 1
    assert my_list.tail.val == 1
    my_list.insert(2)
    assert my_list.head.val == 2
    assert my_list.tail.val == 1


def test_append_node_empty(make_list_empty):
    my_list = make_list_empty
    my_list.append(1)
    assert my_list.head.val == 1
    assert my_list.tail.val == 1


def test_append_node(make_list_three):
    my_list = make_list_three
    my_list.append(0)
    assert my_list.head.val == 3
    assert my_list.tail.val == 0
    my_list.append(-1)
    assert my_list.head.val == 3
    assert my_list.tail.val == -1


def test_pop_empty(make_list_empty):
    with pytest.raises(IndexError):
        make_list_empty.pop()


def test_pop_once(make_list_three):
    my_list = make_list_three
    my_list.pop()
    assert my_list.head.val == 2
    assert my_list.tail.val == 1


def test_pop_twice(make_list_three):
    my_list = make_list_three
    my_list.pop()
    my_list.pop()
    assert my_list.head.val == 1
    assert my_list.tail.val == 1


def test_shift_empty(make_list_empty):
    with pytest.raises(IndexError):
        make_list_empty.shift()


def test_shift_once(make_list_three):
    my_list = make_list_three
    assert my_list.shift() == 1
    assert my_list.head.val == 3
    assert my_list.tail.val == 2


def test_shift_twice(make_list_three):
    my_list = make_list_three
    my_list.shift()
    assert my_list.shift() == 2
    assert my_list.head.val == 3
    assert my_list.tail.val == 3


def test_remove_last(make_list_three):
    my_list = make_list_three
    my_list.remove(1)
    assert my_list.head.next.next is None


def test_remove_first(make_list_three):
    my_list = make_list_three
    my_list.remove(3)
    assert my_list.head.val == 2


def test_remove_middle(make_list_three):
    my_list = make_list_three
    my_list.remove(2)
    assert my_list.head.next.val == 1
