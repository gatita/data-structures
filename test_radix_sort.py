# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from radix_sort import radix_sort


def test_worst_case():
    worst_case = [random.randint(10**3, 10**4) for x in range(10000)]
    assert radix_sort(worst_case) == sorted(worst_case)


def test_random():
    random_case = [random.randint(0, 50) for i in range(50)]
    assert radix_sort(random_case) == sorted(random_case)


def test_repeating_list():
    repeating = [2] * 50
    assert radix_sort(repeating) == [2] * 50


def test_reversed_sorted():
    reversed_case = range(50, -1, -1)
    assert radix_sort(reversed_case) == range(51)


def test_empty_list():
    assert radix_sort([]) == []


def test_list_len_one():
    assert radix_sort([2]) == [2]