# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import pytest
from priorityq import PriorityQueue as pq, Node as n


@pytest.fixture()
def make_heap_empty():
    return pq()


@pytest.fixture()
def make_heap_one():
    return pq([n(1, 1)])


@pytest.fixture()
def make_heap_three():
    return pq([n(1, 1), n(2, 2), n(3, 3)])


@pytest.fixture()
def make_heap_random():
    return pq([n(5, 5), n(2, 2), n(7, 7), n(1, 1), n(0, 0),
               n(3, 3), n(6, 6), n(8, 8), n(4, 4), n(9, 9)])


def test_create_heap(make_heap_empty):
    heap = make_heap_empty
    assert len(heap) == 0
    assert isinstance(heap, pq)


def test_create_heap_one(make_heap_one):
    heap = make_heap_one
    assert len(heap) == 1
    assert heap.container.heap[0].val == 1


def test_create_heap_three(make_heap_three):
    heap = make_heap_three
    assert len(heap) == 3
    assert heap.container.heap[0].val == 1
    assert heap.container.heap[1].val == 2
    assert heap.container.heap[2].val == 3


def test_push_empty(make_heap_empty):
    heap = make_heap_empty
    assert len(heap) == 0
    heap.insert(5, 5)
    assert heap.container.heap[0].val == 5


def test_push_populated(make_heap_three):
    heap = make_heap_three
    assert len(heap) == 3
    heap.insert(5, 5)
    heap.insert(6, 6)
    heap.insert(7, 7)
    assert heap.container.heap[0].val == 1
    assert heap.container.heap[3].val == 5
    assert heap.container.heap[5].val == 7


def test_make_heap_random():
    heap = pq()
    heap.insert(9, 9)
    heap.insert(8, 8)
    heap.insert(7, 7)
    assert heap.container.heap[0].val == 7
    assert heap.container.heap[1].val == 9
    assert heap.container.heap[2].val == 8


def test_make_heap_big_random(make_heap_random):
    heap = make_heap_random
    assert heap.container.heap[0].val == 0
    assert heap.container.heap[1].val == 1
    assert heap.container.heap[2].val == 3
    assert heap.container.heap[3].val == 4
    assert heap.container.heap[4].val == 2
    assert heap.container.heap[5].val == 7
    assert heap.container.heap[6].val == 6
    assert heap.container.heap[7].val == 8
    assert heap.container.heap[8].val == 5
    assert heap.container.heap[9].val == 9


def test_pop_empty(make_heap_empty):
    heap = make_heap_empty
    with pytest.raises(IndexError):
        heap.pop()


def test_pop_populated(make_heap_three):
    heap = make_heap_three
    heap.pop()
    assert heap.container.heap[0].val == 2
    assert heap.container.heap[1].val == 3


def test_pop_twice(make_heap_three):
    heap = make_heap_three
    heap.pop()
    heap.pop()
    assert heap.container.heap[0].val == 3


def test_pop_push_pop(make_heap_three):
    heap = make_heap_three
    heap.pop()
    heap.pop()
    heap.pop()
    heap.insert(5, 5)
    heap.insert(3, 3)
    heap.insert(1, 1)
    assert heap.container.heap[0].val == 1
    assert heap.container.heap[1].val == 5
    assert heap.container.heap[2].val == 3


def test_adding_same_values(make_heap_random):
    heap = make_heap_random
    heap.pop()
    heap.pop()
    heap.pop()
    heap.insert(1, 1)
    heap.insert(1, 1)
    heap.insert(1, 1)
    assert heap.container.heap[0].val == 1
    assert heap.container.heap[1].val == 1
    assert heap.container.heap[2].val == 6
    assert heap.container.heap[3].val == 1
    assert heap.container.heap[4].val == 3
    assert heap.container.heap[5].val == 7
    assert heap.container.heap[6].val == 8
    assert heap.container.heap[7].val == 5
    assert heap.container.heap[8].val == 4
    assert heap.container.heap[9].val == 9


def test_same_priority_different_values(make_heap_three):
    heap = make_heap_three
    heap.insert(7, 0)
    heap.insert(8, 0)
    heap.insert(9, 0)
    assert heap.container.heap[0].priority == 0
    assert heap.container.heap[1].priority == 0
    assert heap.container.heap[2].priority == 0
    assert heap.container.heap[3].priority == 2
    assert heap.container.heap[4].priority == 1
    assert heap.container.heap[5].priority == 3


def test_priority_pop_insert(make_heap_random):
    heap = make_heap_random
    heap.pop()
    heap.pop()
    heap.pop()
    heap.insert(1, 1)
    heap.insert(1, 1)
    heap.insert(1, 1)
    assert heap.container.heap[0].priority == 1
    assert heap.container.heap[1].priority == 1
    assert heap.container.heap[2].priority == 6
    assert heap.container.heap[3].priority == 1
    assert heap.container.heap[4].priority == 3
    assert heap.container.heap[5].priority == 7
    assert heap.container.heap[6].priority == 8
    assert heap.container.heap[7].priority == 5
    assert heap.container.heap[8].priority == 4
    assert heap.container.heap[9].priority == 9


def test_peek(make_heap_three):
    heap = make_heap_three
    assert heap.peek().val == 1


def test_peek_empty(make_heap_empty):
    heap = make_heap_empty
    with pytest.raises(IndexError):
        heap.peek()
