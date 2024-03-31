# Exercises: Level 1
### Explain the difference between map, filter, and reduce.

numbers = [1, 2, 4, 5, 6]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

numbers2 = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers2)
print(list(even_numbers))

### Explain the difference between higher order function, closure and decorator

from functools import reduce

numbers3 = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers3)
print(sum_of_numbers)

### Define a call function before map, filter or reduce, see examples.

def call(func, sequence):
    return [func(item) for item in sequence]

def square(x):
    return x * x

numbers4 = [1, 4, 67, 7, 3]
result = call(square, numbers4)
print(result)

### Use for loop to print each country in the countries list.

countries = ['East Blue', 'North Blue', 'South Blue', 'West Blue']

print("Countries in One Piece universe:")

for country in countries:
    print(country)

### Use for to print each name in the names list.

names = ['Luffy', 'Zoro', 'Nami', 'Usopp', 'Sanji', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jinbei']

print("\nCharacters from One Piece:")

for name in names:
    print(name)

### Use for to print each number in the numbers list.

print("\nNumbers:")
for number in numbers:
    print(number)

# Exercises: Level 2
### List of countries

countries = ['East Blue', 'North Blue', 'South Blue', 'West Blue']

### Map to create a new list by changing each country to uppercase

uppercase_countries = list(map(str.upper, countries))
print("Uppercase countries:", uppercase_countries)

### List of numbers

numbers = [1, 2, 3, 4, 5]

### Map to create a new list by changing each number to its square

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

### List of names

names = ['Luffy', 'Zoro', 'Nami', 'Usopp', 'Sanji', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jinbei']

### Map to change each name to uppercase

uppercase_names = list(map(str.upper, names))
print("Uppercase names:", uppercase_names)

### Filter to filter out countries containing 'land'

filtered_countries1 = list(filter(lambda x: 'land' not in x.lower(), countries))
print("Countries without 'land':", filtered_countries1)

### Filter to filter out countries having exactly six characters

filtered_countries2 = list(filter(lambda x: len(x) != 6, countries))
print("Countries not having exactly six characters:", filtered_countries2)

### Filter to filter out countries containing six letters and more

filtered_countries3 = list(filter(lambda x: len(x) >= 6, countries))
print("Countries containing six letters and more:", filtered_countries3)

### Filter to filter out countries starting with an 'E'

filtered_countries4 = list(filter(lambda x: not x.startswith('E'), countries))
print("Countries not starting with 'E':", filtered_countries4)

### Chain two or more list iterators

from functools import reduce

arr = ['a', 'b', 'c', 'd', 'e']
result = reduce(lambda acc, val: acc + val.upper(), map(lambda x: x.upper(), filter(lambda x: x != 'c', arr)), '')
print("Chained result:", result)

### Declare a function called get_string_lists

def get_string_lists(arr):
    return list(filter(lambda x: isinstance(x, str), arr))

### Use reduce to sum all the numbers in the numbers list

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

### Use reduce to concatenate all the countries

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries)
print("Concatenated countries:", concatenated_countries, "are north European countries")

### Declare a function called categorize_countries

def categorize_countries(countries):
    return list(filter(lambda x: 'land' in x or x.endswith('ia') or 'island' in x or x.endswith('stan'), countries))

### Create a function returning a dictionary

def get_countries_starting_with(countries):
    result = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1
    return result

### Declare a get_first_ten_countries function

def get_first_ten_countries():
    with open('data/countries.txt', 'r') as file:
        return [next(file).strip() for _ in range(10)]

### Declare a get_last_ten_countries function
    
def get_last_ten_countries():
    with open('Level-1\30 Day Python Challenge\Day 14 - Higher Order Functions\countries_data.py', 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines[-10:]]

### Test the functions
    
arr = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 'f', 'g']
print("String items in the list:", get_string_lists(arr))

countries = ['England', 'Finland', 'Mongolia', 'Thailand', 'Pakistan', 'Ireland', 'Scotland']
print("Categorized countries:", categorize_countries(countries))

print("Number of countries starting with each letter:", get_countries_starting_with(countries))

print("First ten countries:", get_first_ten_countries())
print("Last ten countries:", get_last_ten_countries())
