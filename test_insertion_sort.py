# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import random
from insertion_sort import insertion_sort


@pytest.fixture
def normal_list():
    return [random.randint(0, 100) for i in range(15)]


@pytest.fixture
def repeating_list():
    return [4] * 15


@pytest.fixture
def sorted_list():
    return range(15)


@pytest.fixture
def worst_case():
    return range(15, -1, -1)


def test_normal_case(normal_list):
    assert insertion_sort(normal_list) == sorted(normal_list)


def test_repeating_list(repeating_list):
    assert insertion_sort(repeating_list) == [4] * 15


def test_sorted_list(sorted_list):
    assert insertion_sort(sorted_list) == range(15)


def test_reversed_list(worst_case):
    assert insertion_sort(worst_case) == range(16)
