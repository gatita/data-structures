# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from timeit import timeit


def insertion_sort(l):
    for i in range(1, len(l)):
        index = i
        val = l[i]
        while index > 0 and val < l[index-1]:
            l[index] = l[index-1]
            index -= 1
        l[index] = val
    return l


if __name__ == '__main__':
    best_case = range(10000)
    worst_case = range(10000, -1, -1)

    setup = 'from __main__ import insertion_sort, best_case, worst_case'

    print 'best case: ', timeit(
        'insertion_sort(best_case)',
        setup=setup,
        number=1)

    print 'worst_case: ', timeit(
        'insertion_sort(worst_case)',
        setup=setup,
        number=1)
