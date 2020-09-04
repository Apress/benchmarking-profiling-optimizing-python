import random
import timeit

numbers = list(random.random() for _ in range(1000))

def bubblesort(numbers):
    to_sort = numbers[:]
    for target in range(len(to_sort) - 1, 1, -1):
        for j in range(target):
            if to_sort[j] > to_sort[j + 1]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
    return to_sort

assert sorted(numbers) == bubblesort(numbers)

setup = 'from __main__ import numbers, bubblesort'
for statement in 'sorted(numbers)', 'bubblesort(numbers)':
    print(statement, timeit.timeit(setup=setup, stmt=statement, number=5))
