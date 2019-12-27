'''
name = input("Enter your name: ")  # generates prompt; takes inputted user value and puts it into a variable called name
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)  # uses stored variables to show prompt

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)  # float added to take an number. decimal or whole
print(result)  # show final input
'''

try:
    print(10 / 0)  # can be removed to show second except
    number = int(input(" Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("That's not a number")

