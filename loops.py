is_male = True
is_tall = True

if is_male and is_tall :
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not mall or not tall or both")

i = 1  # set defined value for i
while i <= 10:  # will check if i is less than or equal to 10
    print(i)  # will print i until condition is met
    i += 1  # same as i = i + 1. This will keep adding 1 to i until i <=10

print("Done With Loop")  # after all conditions are met then this will print

# ------------------------------------------------------------------------------

friends = ["Cody", "Allen", "Jack", "Quinn", "Zach"]
for index in friends:  # to access "friend" you have to print the same name
    print(index)  # needs to match

for index in range(len(friends)):  # counts til 10
    print(index)  # needs to match
