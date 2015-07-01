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


def test_push():
    pass


def test_pop():
    pass
