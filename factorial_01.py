import timeit

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def list_factorials(n):
    return [factorial(i) for i in range(n + 1)]

print(list_factorials(10))

setup = 'from __main__ import list_factorials'
statement = 'list_factorials(60)'
duration = timeit.timeit(statement, setup=setup, number=1000)
print(f'No caching, First 60, duration: {duration}')
