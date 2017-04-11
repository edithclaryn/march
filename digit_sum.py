"""Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

(Assume that the number you are given will always be positive.)"""
def digit_sum(n):
    number = n
    result = 0
    while number > 0:
        remainder = number % 10
        result += remainder
        number = number // 10
    return result
print (digit_sum(1234))
