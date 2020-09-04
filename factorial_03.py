import timeit

cache = {}

def factorial(n):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        else:
            cache[n] = n * factorial(n - 1)
    return cache[n]

def list_factorials(n):
    global cache
    cache = {}
    return [factorial(i) for i in range(1, n + 1)]

print(list_factorials(10))

setup = 'from __main__ import list_factorials'
statement = 'list_factorials(60)'
duration = timeit.timeit(statement, setup=setup, number=1000)
print(f'Manual caching, recursive, duration: {duration}')
