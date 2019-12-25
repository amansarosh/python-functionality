import turtle  # used for drawing board
from math import *

print("Hello World")  # Hello World Print Line
print("Line 1\nLine 2")  # Newline
print("Line 1\"Line 2\"")  # Quotation Mark

phrase = "Test Phrase"
print(phrase + " hello world")

phrase = "TEST PHRASE"
print(phrase.lower())

phrase = "TEST PHRASE"
print(phrase.islower())

phrase = "TEST PHRASE"
print(phrase.isupper())

phrase = "Test Phrase"
print(phrase.upper().isupper())

phrase = "test phrase"
print(phrase.upper())

phrase = "test phrase"
print(len(phrase))

phrase = "test phrase"
print(phrase[0])

phrase = "test phrase"
print(phrase.index("phr"))

phrase = "test phrase"
print(phrase.replace("test", "plane"))
# ___________Story With Variables__________________________

character_name = "John"  # character_name variable
character_age = "35"  # character_age variable
is_male = True  # true or false bool. Starting letter needs to be capitalized

print("There was once a man named " + character_name + ", ")
print("He was only " + character_age + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ". ")
print("But he didn't like being " + character_age + ". ")

# ___________Shapes__________________________

print("    /_|")
print("   /__|")  # Triangle Shape
print("  /___|")
print(" /____|")

# ___________Math Operations__________________________

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
print(4/3)  # division
print(3 * 4 + 5)  # order of operations (PEMDA(S))
print(3 * (4 + 5))  # multiple math operations using "()"
print(10 % 3)  # read as "10 mod 3" takes 10/3 and gives remainder.
