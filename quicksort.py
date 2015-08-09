# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from timeit import timeit
import random
import sys

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

    while True:
        while list_[i] <= pivot and i != hi:
            i += 1
        while list_[j] >= pivot and j != lo:
            j -= 1
        if i < j:
            list_[i], list_[j] = list_[j], list_[i]
        else:
            list_[lo], list_[j] = list_[j], list_[lo]
            return j


if __name__ == '__main__':
    sys.setrecursionlimit(3000)

    # Best and worst cases for Hoare partition scheme
    worst_case = range(1000)
    best_case = range(1000)
    random.shuffle(best_case)

    setup = 'from __main__ import quicksort, best_case, worst_case'

    print 'best case, pivot = l[0], hoare partition: ', timeit(
        'quicksort(best_case)',
        setup=setup,
        number=100)

    print 'worst case, pivot = l[0], hoare partition: ', timeit(
        'quicksort(worst_case)',
        setup=setup,
        number=100)
