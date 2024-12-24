import math

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Base a must be > 0 and != 1, and b must be > 0")
    return math.log(b, a)

def ln(b):
    if b <= 0:
        raise ValueError("Input must be > 0")
    return math.log(b)

def lg(b):
    if b <= 0:
        raise ValueError("Input must be > 0")
    return math.log10(b)
