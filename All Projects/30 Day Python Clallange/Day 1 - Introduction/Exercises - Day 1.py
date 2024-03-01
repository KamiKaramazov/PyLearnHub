### Exercise: Level 1
# Check the python version you are using

import sys

print("Python version is: ",(sys.version) )

# Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3+4)
print(3-4)
print(3/4)
print(3*4)
print(3**4)
print(3//4)
print(3%4)

# Write strings on the python interactive shell. The strings are the following: "Your name, Your family name ,Your country, I am enjoying 30 days of python"

name = input("Enter your name: ")
age = input("Enter your age: ")
family_name = input("Enter your family name: ")
country = input("Enter your country: ")
print(f"My name is {name}, I'm {age} years old. {family_name} is one of the my family member and we live in {country}. I'm enjoying 30 days of python ")

# Check the data types of the following data: 10 ,9.8, 3.14, 4 - 4j, ['Asabeneh', 'Python', 'Finland'], Your name, Your family name, Your country

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))

data_type_check = input("Please enter something, I'll tell the data type what you type here: ")
print(f"Your data type is {type(eval(data_type_check))}")

# Euclidean distance calculator

