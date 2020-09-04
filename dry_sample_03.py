import timeit

def sum_function_v1(x, y):
    return 5 * x ** 2 + 3 * y ** 2

def nested_loop_v1():
    total = 0
    for x in range(100):
        for y in range(100):
            total += sum_function_v1(x, y)
    return total

def sum_function_v2(x_squared, y_squared):
    return 5 * x_squared + 3 * y_squared

def nested_loop_v2():
    total = 0
    for x in range(100):
        x_squared = x ** 2
        for y in range(100):
            y_squared = y ** 2
            total += sum_function_v2(x_squared, y_squared)
    return total

for function in nested_loop_v1, nested_loop_v2:
    name = function.__name__
    setup = f'from __main__ import {name}'
    duration = timeit.timeit(f'{name}()', setup=setup, number=100)
    print(f'{name}, result: {function()}, duration: {duration}')
