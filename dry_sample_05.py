import timeit

global_total = 0

def sum_of_sine_v1():
    global global_total
    global_total = 0
    for x in range(10000):
        global_total += x ** 2

def sum_of_sine_v2():
    global global_total
    local_total = 0
    for x in range(10000):
        local_total += x ** 2
    global_total = local_total

for function in sum_of_sine_v1, sum_of_sine_v2:
    name = function.__name__
    setup = f'from __main__ import {name}'
    duration = timeit.timeit(f'{name}()', setup=setup, number=100)
    function()
    print(f'{name}, result: {global_total}, duration: {duration}')
