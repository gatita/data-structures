# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from parenthetics import parenthetics


# test empty string
def test_empty_input():
    assert parenthetics('') == 0


# test open final parentheses
def test_open_end():
    assert parenthetics('((a, b, a))(') == 1


# test open beginning parentheses
def test_open_start():
    assert parenthetics('(()()') == 1


# test balanced parentheses
def test_balanced():
    assert parenthetics('(5+5)(2*2*2)(2)') == 0
    assert parenthetics('((()()))') == 0


# test broken
def test_broken():
    assert parenthetics(')') == -1


def test_broken_long():
    assert parenthetics('(1+1)(3+5)2)(') == -1


# test invalid input
def test_non_interable_input():
    with pytest.raises(TypeError):
        parenthetics(22)
