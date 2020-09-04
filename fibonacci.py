def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
	print(fibonacci(20))
