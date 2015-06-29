# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from parenthetics import parenthetics


def test_empty():
    assert parenthetics('') == 0


def test_balanced():
    assert parenthetics('()') == 0


def test_balanced_unicode():
    assert parenthetics('((︵)(︶))') == 0
    assert parenthetics('((︵)()(︶))') == 0
    assert parenthetics('((︵()()︶))') == 0


def test_open():
    assert parenthetics('(') == 1


def test_open_unicode():
    assert parenthetics('((︵)(︶))(') == 1
    assert parenthetics('(((︵)(︶))') == 1
    assert parenthetics('(︵(()(︶))') == 1


def test_broken():
    assert parenthetics(')') == -1


def test_broken_unicode():
    assert parenthetics('((︵)(︶)))') == -1
    assert parenthetics(')((︵)(︶))') == -1
    assert parenthetics('((︵)()︶))') == -1
