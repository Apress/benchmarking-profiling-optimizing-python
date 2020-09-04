import timeit

cache = {}

def factorial(n):
    if n not in cache:
        result = 1
        for i in range(1, n + 1):
            result *= i

        cache[n] = result
    return cache[n]

def list_factorials(n):
    global cache
    cache = {}
    return [factorial(i) for i in range(n + 1)]

print(list_factorials(10))

setup = 'from __main__ import list_factorials; cache={}'
statement = 'list_factorials(60)'
duration = timeit.timeit(statement, setup=setup, number=1000)
print(f'Manual caching, duration: {duration}')
