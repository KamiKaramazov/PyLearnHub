# Create a Python program that concatenates two variables to form your full name. Store your first name and last name in separate variables and combine them using f-strings.
first_name = "Talha"
last_name = "Sen"
full_name = f"{first_name} {last_name}"
print(full_name)
# Explanation: This program uses f-strings to concatenate the first name and last name and print the full name.

# Write a program that asks the user to enter their first name and last name. Then, create a greeting message using this input and print it using f-strings.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
print(f"Welcome, {full_name}!")
# Explanation: This program takes user input for the first name and last name, then uses f-strings to create a greeting message and prints it.

# Write a program that prompts the user to enter their age and name. Then, create a sentence using this information and print it using f-strings.
first_name = input("Please enter your name: ")
last_name = input("Please enter your last name: ")
full_name = f"{first_name} {last_name}"
age = input("Please enter your age: ")
print(f"My name is {full_name}, and I am {age} years old.")
# Explanation: This program takes user input for name and age, then uses f-strings to create a sentence and prints it.

# Write a program that calculates a user's age based on their birth year and the current year. Use f-strings to display the age.
import datetime
birth_year = int(input("Please enter your birth year (YYYY): "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old!")
# Explanation: This program calculates the age using the current year and birth year and prints it using an f-string.

# Write a program that takes a user's weight in kilograms and converts it to pounds. Display the weight in pounds using f-strings. (1 kilogram = 2.20462 pounds)
current_weight_kg = float(input("Please enter your weight in kilograms: "))
weight_in_pounds = int(current_weight_kg * 2.20462)
print(f"Your weight is {weight_in_pounds} pounds.")
# Explanation: This program converts the weight from kilograms to pounds and prints it using an f-string.
