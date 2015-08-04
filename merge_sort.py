# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from timeit import timeit


def mergesort(l):
    if len(l) <= 1:
        return l
    else:
        middle = len(l)/2
        left = l[:middle]
        right = l[middle:]
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


if __name__ == '__main__':

    # large inputs
    worst_case = [i for i in range(1, 10**6) if i % 2] + \
        [i for i in range(1, 10**6) if not i % 2]
    best_case = range(1, 10000)

    # smaller inputs
    s_worst_case = [i for i in range(1, 50) if i % 2] + \
        [i for i in range(1, 50) if not i % 2]
    s_best_case = range(1, 50)

    setup1 = 'from __main__ import mergesort, worst_case, best_case'
    setup2 = 'from __main__ import mergesort, s_worst_case, s_best_case'

    print 'best case, input size = 10^6: ', timeit(
        'mergesort(best_case)',
        setup=setup1,
        number=1)

    print 'worst case, input size = 10^6: ', timeit(
        'mergesort(worst_case)',
        setup=setup1,
        number=1)

    print 'best case, input size = 50: ', timeit(
        'mergesort(s_best_case)',
        setup=setup2,
        number=10)

    print 'worst case, input size = 50: ', timeit(
        'mergesort(s_worst_case)',
        setup=setup2,
        number=10)
