from math import *  # cannot resolve to containing file

a = 10
b = 20  # addition with variables
print(a + b)

my_numpos = 5
print(str(my_numpos) + ", my favorite number")  # number to string

my_numneg = -5
print(abs(my_numneg))  # absolute value of -5 (5)

print(pow(3, 2))  # same as 3^2 or read as "3 to the power of 2"

print(max(4, 6))  # max number

print(min(4, 6))  # min number

print(round(3.4))  # rounds using standard rounding rules
print(round(3.5))

print(floor(3.9))  # chops decimal off and rounds down NEEDS MATH IMPORT
print(ceil(3.4))  # chops decimal off and rounds up NEEDS MATH IMPORT

print(sqrt(36))  # finds square root of 36 NEEDS MATH IMPORT

print(2)  # printing whole, decimal, and negative numbers.
print(2.0345)
print(-2.0345)

print(3 + 4)  # addition
print(3 - 4)  # subtraction
print(4 * 3)  # multiplication
print(4 / 3)  # division
print(3 * 4 + 5)  # order of operations (PEMDA(S))
print(3 * (4 + 5))  # multiple math operations using "()"
print(10 % 3)  # read as "10 mod 3" takes 10/3 and gives remainder.

print(2 ** 3)  # 2x2x2


def raise_to_power(base_num, pow_num):  # function called "raise_to_power" has base_num, and pow_num parameters

    result = 1  # where we store result of math
    for index in range(pow_num):  # loop through pow_num
        result = result * base_num  # does calculations
    return result


print(raise_to_power(3, 4))  # has values to show correct value
