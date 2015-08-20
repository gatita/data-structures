# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from quicksort import quicksort


def test_worst_case():
    worst_case = range(50)
    assert quicksort(worst_case) == worst_case


def test_random():
    random_case = [random.randint(0, 50) for i in range(50)]
    assert quicksort(random_case) == sorted(random_case)


def test_repeating_list():
    repeating = [2] * 50
    assert quicksort(repeating) == [2] * 50


def test_reversed_sorted():
    reversed_case = range(50, -1, -1)
    assert quicksort(reversed_case) == range(51)


def test_empty_list():
    assert quicksort([]) == []


def test_list_len_one():
    assert quicksort([2]) == [2]
