# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import pytest
import binheap


@pytest.fixture()
def make_heap_empty():
    return binheap.BinaryHeap()


@pytest.fixture()
def make_heap_one():
    return binheap.BinaryHeap([1])


@pytest.fixture()
def make_heap_three():
    return binheap.BinaryHeap([1, 2, 3])


def test_create_heap(make_heap_empty):
    heap = make_heap_empty
    assert len(heap) == 0
    assert isinstance(heap, binheap.BinaryHeap)


def test_create_heap_one(make_heap_one):
    heap = make_heap_one
    assert len(heap) == 1
    assert heap.heap[0] == 1


def test_create_heap_three(make_heap_three):
    heap = make_heap_three
    assert len(heap) == 3
    assert heap.heap[0] == 1
    assert heap.heap[1] == 2
    assert heap.heap[2] == 3


def test_push_empty(make_heap_empty):
    heap = make_heap_empty
    assert len(heap) == 0
    heap.push(5)
    assert heap.heap[0] == 5


def test_push_populated(make_heap_three):
    heap = make_heap_three
    assert len(heap) == 3
    heap.push(5)
    heap.push(6)
    heap.push(7)
    assert heap.heap[0] == 1
    assert heap.heap[3] == 5
    assert heap.heap[5] == 7


def test_make_heap_random():
    heap = binheap.BinaryHeap()
    heap.push(9)
    heap.push(8)
    heap.push(7)
    assert heap.heap[0] == 7
    assert heap.heap[1] == 9
    assert heap.heap[2] == 8


def test_make_heap_big_random():
    heap = binheap.BinaryHeap([5, 2, 7, 1, 0, 3, 6, 8, 4, 9])
    assert heap.heap[0] == 0
    assert heap.heap[1] == 1
    assert heap.heap[2] == 3
    assert heap.heap[3] == 4
    assert heap.heap[4] == 2
    assert heap.heap[5] == 7
    assert heap.heap[6] == 6
    assert heap.heap[7] == 8
    assert heap.heap[8] == 5
    assert heap.heap[9] == 9


def test_pop_empty(make_heap_empty):
    heap = make_heap_empty
    with pytest.raises(IndexError):
        heap.pop()


def test_pop_populated(make_heap_three):
    heap = make_heap_three
    heap.pop()
    assert heap.heap[0] == 2
    assert heap.heap[1] == 3
