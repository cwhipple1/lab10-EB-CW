# https://github.com/elijahbaez/lab10-EB-CW.git
# Partner 1: Elijah Baez
# Partner 2: Curtis Whipple


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def exp(a, b):
    return a ** b

def square_root(a):
    # Calculates the square root of a number.
    # Raises ValueError for negative numbers.
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    # Calculates the hypotenuse of a right triangle given two sides.
    return math.hypot(a, b)

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Logarithm arguments must be positive, and base cannot be 1.")
    return math.log(b, a)
