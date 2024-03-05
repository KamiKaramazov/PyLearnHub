#3-1. Names: Store the names of a few of your friends in a list called names./
#Print each person’s name by accessing each element in the list, one at a time.

names =  ["liam", "noah", "oliver", "james", "olivia", "ava"]
for name in names:
    print(name.title())

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just/
# printing each person’s name, print a message to them. The text of each message/
# should be the same, but each message should be personalized with the person’s name.

names =  ["liam", "noah", "oliver", "james", "olivia", "ava"]
for name in names:
    print(f"{name.title()} is my best friend!")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a/
# motorcycle or a car, and make a list that stores several examples. Use your list/,
# to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

brands = ["tesla", "mazda", "subaru", "porsche", "honda", "lexus", "toyota"]
for i in brands:
    print(f"I like to own a {i.title()}")