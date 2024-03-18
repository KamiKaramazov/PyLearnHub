### Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

user_age = int(input("Enter your age :"))

if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_wait = 18 - user_age
    print(f"You need {years_wait} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    year_diff = my_age - your_age
    print(f"I'm {year_diff} years older than you.")
elif my_age < your_age:
    year_diff = your_age - my_age
    print(f"You are {year_diff} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

number1 = int(input("Enter number one: "))
number2 = int(input("Enter number two: "))

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number1} is less than {number2}")
else:
    print(f"{number1} equal to {number2}")

### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
"""80-100, A
70-79, B
60-69, C
50-59, D
0-49, F"""

user_score = int(input("Please enter your score: "))

if user_score >= 80:
    print("A")
elif user_score >= 70 and user_score <=79:
    print("B")
elif user_score >= 60 and user_score <= 69:
    print("C")
elif user_score >= 50 and user_score <= 59:
    print("D")
else:
    print("F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

import datetime

def get_season_from_timestamp(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    month = dt.month

    if month >= 3 and month <= 5:
        return "Spring"
    elif month >= 6 and month <= 8:
        return "Summer"
    elif month >= 9 and month <= 11:
        return "Autumn"
    else:
        return "Winter"

current_timestamp = datetime.datetime.now().timestamp()
current_season = get_season_from_timestamp(current_timestamp)
print(f"Current season: {current_season}")

# The following list contains some fruits:
"""fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')"""

def check_digit(text):
    if any(char.isdigit() for char in text):
        return True
    else:
        return False

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter fruit name: ")

if check_digit(user_fruit):
    print("Please enter text without numbers!")
elif user_fruit.lower() in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(user_fruit)
    print(f"{user_fruit} added to the current list:", fruits)

### Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
"""        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
* If the person is married and if he lives in Finland, print the information in the following format:
       Asabeneh Yetayeh lives in Finland. He is married.
     """
luffy = {
    'first_name': 'Monkey D.',
    'last_name': 'Luffy',
    'age': 19,
    'country': 'East Blue',
    'is_married': False,
    'skills': ['Haki', 'Gomu Gomu no Mi','Gomu Gomu no Pistol', 'Gomu Gomu no Gatling', 'Gear Second', 'Gear Third', 'Gear Fourth'],
    'address': {
        'island': 'Foosha Village',
        'zipcode': 'unknown'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in luffy:
    skills = luffy['skills']
    if len(skills) % 2 != 0:
        middle_index = len(skills) // 2
        print('Middle skill:', skills[middle_index])

# Check if the person dictionary has skills key, if so check if the person has 'Haki' skill and print out the result.
if 'skills' in luffy:
    if 'Haki' in luffy['skills']:
        print('Haki skill is present in the skills list.')

# Check the person's skills to determine their title
if 'skills' in luffy:
    skills = luffy['skills']
    if set(['Haki', 'Fighting']).issubset(set(skills)):
        print('He is a powerful fighter')
    elif 'Gomu Gomu no Mi' in skills:
        print('He is a Devil Fruit user')
    else:
        print('Unknown title')

# Check if the person is married (which he is not, as Luffy is not married)
if luffy['is_married']:
    print(f"{luffy['first_name']} {luffy['last_name']} is married.")
else:
    print(f"{luffy['first_name']} {luffy['last_name']} is not married.")