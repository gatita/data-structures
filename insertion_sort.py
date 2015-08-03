# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def insertion_sort(l):
    for i in range(len(l) - 1):
        index = i
        val = l[i]
        while index > 0 and l[index-1] > l[index]:
            l[i] = l[i-1]
            index -= 1
        l[index] = val