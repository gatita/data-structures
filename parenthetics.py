# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from stack import Stack


def parenthetics(str):
    """Check for matching opening and closing characters."""

    open_stack = Stack()

    for c in str:
        if c == '(':
            open_stack.push(c)
        elif c == ')':
            try:
                open_stack.pop()
            except:
                # is broken string
                return -1

    # check for balanced string
    try:
        open_stack.pop()
    except:
        return 0

    # open string
    return 1
