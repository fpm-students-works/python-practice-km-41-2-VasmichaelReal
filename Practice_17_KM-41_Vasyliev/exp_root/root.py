import math

def root2(x):
    if x < 0:
        raise ValueError("Input must be a positive number")
    return math.sqrt(x)

def root3(x):
    if x < 0:
        raise ValueError("Input must be a positive number")
    return x ** (1 / 3)
