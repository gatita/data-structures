# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from timeit import timeit
import random
import sys


def radix_sort(list_, base=10):
    if len(list_) == 0:
        return list_
    else:
        place = 1
        max_length = len(str(max(list_)))

    for x in range(max_length):
        buckets = [[] for i in range(base)]

        for i in list_:
            digit = i // place
            buckets[digit % base].append(i)

        list_ = []
        for bucket in buckets:
            list_.extend(bucket)

        place *= base

    return list_


if __name__ == '__main__':
    """
    Time best and worst cases for radix sort, where best case
    is a list of small inputs, and worst case is
    a list of very large inputs.
    """
    best_case = [random.randint(0, 9) for x in range(10000)]
    worst_case = [random.randint(10**3, 10**4) for x in range(10000)]

    setup = 'from __main__ import radix_sort, best_case, worst_case'

    print 'best case: ', timeit(
        'radix_sort(best_case)',
        setup=setup,
        number=100)

    print 'worst case: ', timeit(
        'radix_sort(worst_case)',
        setup=setup,
        number=100)
