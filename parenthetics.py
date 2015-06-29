# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from stack import Stack


def parenthetics(string):
    """
    Takes a unicode string (text) as input and returns one of three
    possible values:
        1: If the string is 'open' (there are open parens that are not closed)
        0: If the string is 'balanced' (there are an equal number of open and
            close parentheses in the string). Will also return 0 if there are
            no parentheses in the string.
        -1: If the string is 'broken' (a closing parens has not been proceeded
            by one that opens)
    """

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
