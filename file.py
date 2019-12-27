
"""
# reads files and lists content inside
employee_file = open("employees", "r")  # r means read; w means write; a means append which lets you add on; r+ lets you read and write

# print(employee_file.readable())  # will return bool value that will tell if the file is readable

for employees in employee_file.readlines():
    print(employees)  # will take all lines from file and will put inside array


employee_file.close()  # when you open the file you want to make sure you close it at some point
"""
employee_file = open("employees", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()
