def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    return n * factorial(n - 1)
