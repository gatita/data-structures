# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from queue import Queue
import pytest


def test_enqueue_empty():
    my_queue = Queue()
    my_queue.enqueue(1)
    print my_queue.container.display()
    assert my_queue.container.head.value == 1


def test_enqueue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    assert my_queue.container.head.value == 1
    assert my_queue.tail.value == 3


def test_dequeue_empty():
    my_queue = Queue()
    with pytest.raises(IndexError):
        my_queue.dequeue()


def test_dequeue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    assert my_queue.container.head.value == 2
    assert my_queue.tail.value == 3


def test_dequeue_twice():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    my_queue.dequeue()
    assert my_queue.container.head.value == 3
    assert my_queue.tail.value == 3


def test_enqueue_dequeue_enqueue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.dequeue()
    my_queue.enqueue(2)
    assert my_queue.container.head.value == 2
    assert my_queue.tail.value == 2


def test_size_empty():
    my_queue = Queue()
    my_queue.enqueue(1)
    assert my_queue.size() == 1


def test_size():
    my_queue = Queue()
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    assert my_queue.size() == 3


def test_size_enqueue_dequeue():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.dequeue()
    my_queue.enqueue(2)
    assert my_queue.size() == 1
