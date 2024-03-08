### Exercises: Level 1
# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
not_empty_tuple = ("Name1", "Name2", "Name3")
# Join brothers and sisters tuples and assign it to siblings
siblings = not_empty_tuple + ("Name4", "Name5")
print(siblings)
# How many siblings do you have?
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = "Father"
mother= "Mother"
siblings = siblings + (father,mother)
print(siblings)

### Exercises: Level 2
# Unpack siblings and parents from family_members
family_members = ("Name1", "Name2", "Name3", "Name4", "Name5", "Father's Name", "Mother's Name")
sibling1, sibling2, sibling3, sibling4, sibling5, father, mother = family_members

print("Sibling 1:", sibling1)
print("Sibling 2:", sibling2)
print("Sibling 3:", sibling3)
print("Sibling 4:", sibling4)
print("Sibling 5:", sibling5)
print("Father:", father)
print("Mother:", mother)

# Create fruits, vegetables, and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach', 'broccoli')
animal_products = ('beef', 'chicken', 'milk')

# Join the three tuples
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle_index] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index-1:middle_index+1]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
estonia_is_nordic = 'Estonia' in nordic_countries
iceland_is_nordic = 'Iceland' in nordic_countries

print("Middle item or items:", middle_item)
print("First three items:", first_three_items)
print("Last three items:", last_three_items)
print("Is Estonia a nordic country?", estonia_is_nordic)
print("Is Iceland a nordic country?", iceland_is_nordic)

