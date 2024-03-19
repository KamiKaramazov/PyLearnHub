### Exercises: Level 1
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2:30 of python programming

# Declare a first name variable and assign a value to it
name = "Kami"
# Declare a last name variable and assign a value to it
last_name = "Sama"
# Declare a full name variable and assign a value to it by concatenating first name and last name
full_name = name + " " + last_name
# Declare a country variable and assign a value to it
country = "Chips"
# Declare a city variable and assign a value to it
city = "Fish"
# Declare an age variable and assign a value to it
age = 31
# Declare a year variable and assign a value to it
year = 2024
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variables on one line
x, y, z = 1, 3, 5
# Print the concatenated values
print(full_name + " lives in " + city + ", " + country + ". He is " + str(age) + " years old in " + str(year) + ". Married: " + str(is_married) + ". Light is on: " + str(is_light_on))

### Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print("Data type of 'full_name' is: ", type(full_name))
print("Data type of 'city' is: ", type(city))
print("Data type of 'country' is: ", type(country))
print("Data type of 'city' is: ", type(city))
print("Data type of 'year' is: ", type(year))
print("Data type of 'is_married': ", type(is_married))
print("Data type of 'is_true': ", type(is_true))
print("Data type of 'is_light_on': ", type(is_light_on))
print("Data type of 'x':", type(x))
print("Data type of 'y':", type(y))
print("Data type of 'z':", type(z))

# Using the len() built-in function, find the length of your first name
print(len(name))

# Compare the length of your first name and your last name
first_name_length = len(name)
last_name_length = len(last_name)

if first_name_length > last_name_length:
    print("\nFirst name is longer than last name.")
elif first_name_length < last_name_length:
    print("\nLast name is longer than first name.")
else:
    print("\nFirst name and last name have the same length.")

# Declare num_one and num_two
num_one = 5
num_two = 4

# Add num_one and num_two
total = num_one + num_two

# Subtract num_two from num_one
diff = num_one - num_two

# Multiply num_two and num_one
product = num_one * num_two

# Divide num_one by num_two
division = num_one / num_two

# Use modulus division to find num_two divided by num_one
remainder = num_two % num_one

# Calculate num_one to the power of num_two
exp = num_one ** num_two

# Find floor division of num_one by num_two
floor_division = num_one // num_two

# Print the results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius ** 2
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius
# Take radius as user input and calculate the area.
print("Area of the circle: ", area_of_circle)

# Get user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

# Display the information
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
        