# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Samsung", "CISCO"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)

# What is the difference between remove and discard
it_companies.remove('Apple')
print(it_companies)

it_companies.remove('Twitter') 
it_companies.discard('Facebook')
print(it_companies)

it_companies.discard('Twitter') 
print(it_companies)

### Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
intersection = A.intersection(B)
print(intersection)

# Is A subset of B
is_subset = A.issubset(B)

print(is_subset)

# Are A and B disjoint sets?
is_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", is_disjoint)

# Join A with B and B with A
union_AB = A.union(B)
union_BA = B.union(A)
print("Union of A and B:", union_AB)
print("Union of B and A:", union_BA)

# What is the symmetric difference between A and B?
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# Delete the sets completely
del A
del B

### Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
if len(age) > len(set_age):
    print("The length of the list is bigger.")
elif len(age) < len(set_age):
    print("The length of the set is bigger.")
else:
    print("Both have the same length.")

# Explain the difference between the following data types: string, list, tuple and set
# String
name = "John"
print("String:", name)

# List
numbers_list = [1, 2, 3, 4, 5]
print("List:", numbers_list)

# Tuple
colors_tuple = ("red", "green", "blue")
print("Tuple:", colors_tuple)

# Set
unique_numbers_set = {1, 2, 3, 4, 5}
print("Set:", unique_numbers_set)

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))

