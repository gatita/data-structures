# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def mergesort(l):
    if len(l) <= 1:
        return l
    else:
        middle = len(l)/2
        left = l[:middle]
        right = l[middle:]
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    pass
