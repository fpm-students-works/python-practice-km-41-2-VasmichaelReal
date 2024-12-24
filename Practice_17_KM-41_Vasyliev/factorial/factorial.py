def fact(n):
    if n < 0 or not isinstance(n, int):
        raise ValueError("Input must be a natural number (integer >= 0)")
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
