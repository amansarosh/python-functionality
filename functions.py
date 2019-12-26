
def say_hi(name, age):  # when creating a function we need to start with "def" and then function name followed by "()" and a ":"
    print("Hello " + name + ", you are " + str(age))  # what goes inside the function needs to indented


say_hi("Mike", 25)  # call the function with parameters
say_hi("Steve", 40)

# functions should be lowercase
# when using more than 2 words; function names should have an "_"

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print((max_num(34, 45, 56)))

# "==" means equal
# "!=" means "not equal"
