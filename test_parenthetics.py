# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from parenthetics import parenthetics


def test_balanced():
    assert parenthetics('()') == 0


def test_open():
    assert parenthetics('(') == 1


def test_broken():
    assert parenthetics(')') == -1
