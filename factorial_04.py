import timeit
import functools

@functools.lru_cache()
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def list_factorials(n):
    return [factorial(i) for i in range(1, n + 1)]

print(list_factorials(10))

setup = 'from __main__ import list_factorials'
statement = 'list_factorials(60)'
duration = timeit.timeit(statement, setup=setup, number=1000)
print(f'Manual caching, recursive, duration: {duration}')
