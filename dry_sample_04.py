import math
import timeit


def sum_of_sine_v1():
    total = 0
    for x in range(10000):
        total += math.sin(x)
    return total


def sum_of_sine_v2():
    total = 0
    local_sine = math.sin
    for x in range(10000):
        total += local_sine(x)
    return total


for function in sum_of_sine_v1, sum_of_sine_v2:
    name = function.__name__
    setup = f'from __main__ import {name}'
    duration = timeit.timeit(f'{name}()', setup=setup, number=100)
    print(f'{name}, result: {function()}, duration: {duration}')
