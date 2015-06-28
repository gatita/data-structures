# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest
from stack import Stack


# test create empty stack
def test_create_stack_empty():
    my_stack = Stack()
    assert isinstance(my_stack, Stack)
    # assert my_stack.container.display() == ()
    with pytest.raises(IndexError):
        my_stack.pop()


# test create stack with values
def test_create_stack():
    my_stack = Stack([1, 2, 3])
    assert isinstance(my_stack, Stack)
    assert my_stack.pop() == 3
    assert my_stack.pop() == 2
    assert my_stack.pop() == 1


# test push to empty stack
def test_push_to_empty_stack():
    my_stack = Stack()
    # assert my_stack.container.display() == ()
    with pytest.raises(IndexError):
        my_stack.pop()
    my_stack.push(1)
    # assert my_stack.container.display() == (1,)
    assert my_stack.pop() == 1
    my_stack.push(2)
    # assert my_stack.container.display() == (2, 1)
    assert my_stack.pop() == 2


# test push to stack with values
def test_push():
    my_stack = Stack([1, 2, 3])
    my_stack.push(4)
    # assert my_stack.container.display() == (4, 3, 2, 1)
    assert my_stack.pop() == 4
    # check to make sure new stack wasn't initialized
    assert my_stack.pop() == 3


# test push  with no value passed in
def test_push_no_value():
    my_stack = Stack([1, 2, 3])
    with pytest.raises(TypeError):
        my_stack.push()


# test push too many values
def test_push_more_than_one():
    my_stack = Stack([1, 2, 3])
    with pytest.raises(TypeError):
        my_stack.push(2, 3)


# test pop from empty stack
def test_pop_from_empty_stack():
    my_stack = Stack()
    with pytest.raises(IndexError):
        my_stack.pop()


# test pop from stack with values
def test_pop():
    my_stack = Stack([1, 2, 3])
    assert my_stack.pop() == 3


# test popping stack twice
def test_pop_twice():
    my_stack = Stack([1, 2, 3])
    my_stack.pop()
    assert my_stack.pop() == 2
