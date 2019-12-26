lucky_numbers = [24, 8, 12, 16, 20, 4]
friends = ["Cody", "Allen", "Jack", "Quinn", "Zach"]

friends2 = friends.copy()  # Copy List

friends.sort()  # A-Z

friends.pop()  # Removes Last Element from List

friends.remove("Jack")  # removes Jack from List

friends.append("Marc")  # Add Marc to the end of the Array/List

friends.insert(1, "Travis")  # Insert Travis After 0

friends.extend(lucky_numbers)  # Add Array of Lucky Numbers to the end of a List

friends[4] = "Mike"  # Add Mike to the 4th Position

print(friends[-1])  # indexes from back of the list (Zach/Mike)

print(friends[0:4])  # starts from Cody onwards but does not include Zach/Mike

print(friends)  # extend the array to the numbers

print(friends.index("Quinn"))  # This will tell me where in the list Jack is

print(friends.count("Quinn"))   # how many times "quin" is listed

print(friends2)  # prints friends copy

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)
