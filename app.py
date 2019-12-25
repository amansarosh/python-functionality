import turtle  # used for drawing board

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
print(phrase.index("t"))

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
print(a+b)
