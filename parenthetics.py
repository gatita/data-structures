# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from stack import Stack


def parenthetics(string):
    my_stack = Stack()
    for char in string:
        if char == '(':
            my_stack.push(char)
        elif char == ')':
            try:
                my_stack.pop()
            except IndexError:
                return -1
    try:
        my_stack.pop()
    except IndexError:
        return 0
    return 1


if __name__ == '__main__':
    print parenthetics('())')
    print parenthetics('(())')
    print parenthetics('(())(')
    print parenthetics('')
