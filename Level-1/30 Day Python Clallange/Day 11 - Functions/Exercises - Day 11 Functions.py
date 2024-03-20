# Exercises: Level 1
### Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(n1,n2):
    return n1 +n2

result = add_two_numbers(10,13)
print(result)

### Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math

def area_of_circle(r):
    area = math.pi * r * r 
    return area

result = area_of_circle(5)
print("Area of the circle:", result)

### Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"Error: '{num}' is not a number.")
            return None
    return total

nums = input("Enter numbers separated by spaces: ")
nums = [float(num) for num in nums.split()]
result = add_all_nums(*nums)
if result is not None:
    print("Total:", result)

### Temperature conversion from Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(25))

### Check season based on month
def check_season(month):
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    elif month in [12, 1, 2]:
        return "Winter"
    else:
        return "Invalid month"

print(check_season(3))

### Calculate slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope(1, 2, 3, 4))

### Solve quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real roots"

print(solve_quadratic_eqn(1, -3, 2)) 

### Print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3, 4, 5])

### Reverse a list using loops
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))

### Capitalize each item in a list
def capitalize_list_items(lst):
    capitalized_lst = [item.capitalize() for item in lst]
    return capitalized_lst

original_list = ['apple', 'banana', 'cherry']
capitalized_list = capitalize_list_items(original_list)
print(capitalized_list)

### Add an item to a list
def add_item(lst, item):
    lst.append(item)
    return lst

### Remove an item from a list
def remove_item(lst, item):
    lst.remove(item)
    return lst

### Sum of numbers in a range
def sum_of_numbers(n):
    return sum(range(1, n+1))

### Sum of odd numbers in a range
def sum_of_odds(n):
    return sum(range(1, n+1, 2))

### Sum of even numbers in a range
def sum_of_even(n):
    return sum(range(2, n+1, 2))

# Exercises: Level 2
### Count the number of evens and odds in a positive integer
def evens_and_odds(n):
    evens = sum(1 for digit in str(n) if int(digit) % 2 == 0)
    odds = len(str(n)) - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))

### Calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

### Check if a parameter is empty or not
def is_empty(param):
    return not bool(param)

print(is_empty([]))

### Calculate mean of a list
def calculate_mean(lst):
    return sum(lst) / len(lst)

print(is_empty([1, 2, 3]))

### Calculate median of a list
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

print(calculate_mean([1, 2, 3, 4, 5]))

### Calculate mode of a list
def calculate_mode(lst):
    mode_count = {}
    for item in lst:
        if item in mode_count:
            mode_count[item] += 1
        else:
            mode_count[item] = 1
    max_count = max(mode_count.values())
    mode = [key for key, value in mode_count.items() if value == max_count]
    return mode

print(calculate_median([1, 3, 2, 4, 5]))

### Calculate range of a list
def calculate_range(lst):
    return max(lst) - min(lst)

print(calculate_mode([1, 2, 2, 3, 3, 3, 4]))

### Calculate variance of a list
def calculate_variance(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

print(calculate_range([1, 2, 3, 4, 5]))

### Calculate standard deviation of a list
def calculate_std(lst):
    variance = calculate_variance(lst)
    std_dev = variance ** 0.5
    return std_dev

print(calculate_variance([1, 2, 3, 4, 5]))

# Exercises: Level 3
### Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(17))  # True
print(is_prime(21))  # False

### Check if all items in a list are unique
def are_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_items_unique([1, 2, 3, 4]))  # True
print(are_items_unique([1, 2, 2, 4]))  # False

### Check if all items in a list are of the same data type
def are_items_same_type(lst):
    return len(set(type(item) for item in lst)) == 1

print(are_items_same_type([1, 2, 3]))  # True
print(are_items_same_type([1, 'two', 3]))  # False

### Check if a provided variable is a valid Python variable
def is_valid_variable(variable):
    import re
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None

print(is_valid_variable('valid_variable'))  # True
print(is_valid_variable('invalid variable'))  # False

### Importing data from countries-data.py file and returning the most spoken languages in the world
def most_spoken_languages():
    import countries_data
    language_count = {}
    for country_info in countries_data.country_info:
        for language in country_info.get('languages', []):
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    return sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

top_languages = most_spoken_languages()
print(top_languages)

### Importing data from countries-data.py file and returning the most populated countries
def most_populated_countries():
    import countries_data
    return sorted(countries_data.country_info, key=lambda x: x.get('population', 0), reverse=True)[:10]

print(most_populated_countries())