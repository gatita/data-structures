# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''resources:
http://algs4.cs.princeton.edu/23quicksort/Quick.java.html
'''


def quicksort(list_, lo=0, hi=None):
    if hi is None:
        hi = len(list_) - 1
    if lo < hi:
        split = _partition(list_, lo, hi)
        quicksort(list_, lo, split-1)
        quicksort(list_, split+1, hi)
    return list_


def _partition(list_, lo, hi):
    pivot = list_[lo]
    i = lo + 1
    j = hi
    print 'starting: ', list_[lo:hi+1]

    while True:
        print i, j
        while list_[i] <= pivot and i != hi:
            i += 1
            print "i: ", i
        while list_[j] >= pivot and j != lo:
            j -= 1
            print "j: ", j
        if i < j:
            list_[i], list_[j] = list_[j], list_[i]
            print list_
        else:
            list_[lo], list_[j] = list_[j], list_[lo]
            print list_
            print 'split: ', j
            return j
