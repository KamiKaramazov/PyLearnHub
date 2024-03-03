### Exercises: Day 3
# Declare your age as integer variable
age = 22
# Declare your height as a float variable
height = 177
# Declare a variable that store a complex number
number = 134324
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height_triangle
print("The area of the triangle is: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a: ")) 
side_b = float(input("Enter side b: ")) 
side_c = float(input("Enter side c: ")) 
perimeter = side_a + side_b + side_c
print("Perimeter is: ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area is {area} adn the perimeter {perimeter}.")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius: "))
circle = float(input("Enter the circle: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2  
b = -2  
slope = m
x_intercept = -b / m
y_intercept = b

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Slope:", slope)
print("Euclidean distance between the points:", euclidean_distance)

# Compare the slopes in tasks 8 and 9.
m1 = 2  
b1 = -2  
slope1 = m1
x_intercept1 = -b1 / m1
y_intercept1 = b1

print("Slope of y = 2x - 2:", slope1)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)

print("Slope between (2, 2) and (6, 10):", slope2)


if slope1 > slope2:
    print("Slope of y = 2x - 2 is greater than the slope between (2, 2) and (6, 10).")
elif slope1 < slope2:
    print("Slope between (2, 2) and (6, 10) is greater than the slope of y = 2x - 2.")
else:
    print("Slopes are equal.")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def calculate_y(x):
    return x**2 + 6*x + 9
x_value_for_y_zero = -3  

print("At x =", x_value_for_y_zero, ", y is 0.")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len("python")
length_dragon = len("dragon")
falsy_comparison = length_python != length_dragon
print("Is the length of 'python' equal to the length of 'dragon'?", falsy_comparison)

# Use and operator to check if 'on' is found in both 'python' and 'dragon':
check_on = "on" in "python" and "on" in "dragon"
print("Is 'on' found in both 'python' and 'dragon'?", check_on)

# Use in operator to check if 'jargon' is in the sentence:
sentence = "I hope this course is not full of jargon."
check_jargon = "jargon" in sentence
print("Is 'jargon' in the sentence?", check_jargon)

# Find the length of the text 'python' and convert the value to float and then to string:
length_python = len("python")
length_python_float_string = str(float(length_python))
print("Length of 'python' as float and then as string:", length_python_float_string)

# # How to check if a number is even or not using Python:
def is_even(number):
    return number % 2 == 0

number = 6
print(number, "is even?", is_even(number))

# Check if the floor division of 7 by 3 is equal to the integer converted value of 2.7
check_floor_division = 7 // 3 == int(2.7)
print("Is the floor division of 7 by 3 equal to the integer converted value of 2.7?", check_floor_division)

# Check if the type of '10' is equal to the type of 10
check_type = type('10') == type(10)
print("Is the type of '10' equal to the type of 10?", check_type)

# Check if int('9.8') is equal to 10
check_int_conversion = int('9.8') == 10
print("Is int('9.8') equal to 10?", check_int_conversion)

# Write a script that prompts the user to enter hours and rate per hour. Calculate the pay of the person
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is", pay)

# Write a script that prompts the user to enter the number of years and calculate the number of seconds a person can live, assuming they can live a hundred years
years = int(input("Enter number of years you have lived: "))
seconds_per_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_per_year
print("You have lived for", total_seconds, "seconds.")

# Display the table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
