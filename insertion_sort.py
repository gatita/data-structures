# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(l):
    for i in range(1, len(l)):
        index = i
        val = l[i]
        while index > 0 and val < l[index-1]:
            l[index] = l[index-1]
            index -= 1
        l[index] = val
    return l
