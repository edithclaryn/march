"""Define a function factorial that takes an integer x as input.

Calculate and return the factorial of that number."""
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)