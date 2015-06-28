# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from stack import Stack


def parenthetics(str):
    open_chars = '('
    close_chars = ')'

    open_stack = Stack()

    for c in str:
        if c in open_chars:
            open_stack.push(c)
        elif c in close_chars:
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


if __name__ == '__main__':
    print(parenthetics('()'))           # 0
    print(parenthetics('())'))          # -1
    print(parenthetics('(()'))          # 1
