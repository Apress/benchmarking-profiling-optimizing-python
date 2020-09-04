import timeit

def nested_loop_v1():
    total = 0
    for x in range(100):
        for y in range(100):
            x_squared = x ** 2
            y_squared = y ** 2
            total += x_squared + y_squared
    return total

def nested_loop_v2():
    total = 0
    for x in range(100):
        x_squared = x ** 2
        for y in range(100):
            y_squared = y ** 2
            total += x_squared + y_squared
    return total

for function in nested_loop_v1, nested_loop_v2:
    name = function.__name__
    setup = f'from __main__ import {name}'
    duration = timeit.timeit(f'{name}()', setup=setup, number=100)
    print(f'{name}, result: {function()}, duration: {duration}')
