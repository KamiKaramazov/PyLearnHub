### 6-1. Person: 
# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

pearson = {"first name": "Monkey D.", "last name": "Luffy", "age": "19", "city": "East Blue"}

for key, value in pearson.items():
    print(f"{key.title()}: {value}\n")

### 6-2. Favorite Numbers: 
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
    
favorite_numbers = {"Monkey D. Luffy": 56, "Roronora Zoro": 3, "Nami": 10, "Usopp": 800, "Sanji": 77}

for key, value in favorite_numbers.items():
    print(f"{key}:{value}\n")

### 6-3. Glossary: 
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
    
glossary = {
    "variable": "A named storage location in memory that holds a value.",
    "list": "A collection of items that can be stored and manipulated individually.",
    "function": "A named block of code that performs a specific task when called.",
    "loop": "A control flow statement for iterating over a sequence of elements.",
    "dictionary": "A collection of key-value pairs, where each key is associated with a value."
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

### 6-4. Glossary 2: 
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
    
glossary = {
    "variable": "A named storage location in memory that holds a value.",
    "list": "A collection of items that can be stored and manipulated individually.",
    "function": "A named block of code that performs a specific task when called.",
    "loop": "A control flow statement for iterating over a sequence of elements.",
    "dictionary": "A collection of key-value pairs, where each key is associated with a value."
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

additional_terms = {
    "module": "A file containing Python code that can be imported and used in other Python files.",
    "class": "A blueprint for creating objects, providing initial values and behaviors.",
    "method": "A function that is associated with an object and can access its data.",
    "inheritance": "A mechanism in which a new class is derived from an existing class.",
    "exception": "An event that occurs during the execution of a program and disrupts its normal flow."
}

glossary.update(additional_terms)
print("\nUpdated Glossary:")
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

### 6-5. Rivers: 
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for rivers, country in major_rivers.items():
    print(f"The {rivers} runs through {country}.")

### 6-6. Polling: 
# Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, you are invited to take the favorite languages poll!")
    
new_user = input("Enter your name: ")
user_language = input("Enter your favorite programming language: ")

favorite_languages[new_user.lower()] = user_language.lower()

for key, value in favorite_languages.items():  
    print(f"{key.title()}: {value.title()}")  

### 6-7. People: 
# Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

pearson1 = {"first name": "Monkey D.", "last name": "Luffy", "age": "19", "city": "East Blue"}
new_person2 = {"first name": "Roronoa", "last name": "Zoro", "age": "21", "city": "Shimotsuki Village"}
new_person3 = {"first name": "Nami", "last name": "Unknown", "age": "20", "city": "Cocoyasi Village"}
new_person4 = {"first name": "Vinsmoke", "last name": "Sanji", "age": "21", "city": "Baratie"}

people = [pearson1, new_person2, new_person3, new_person4]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")

### 6-8. Pets: 
# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pet1 = {"animal": "Dog", "owner": "Alice"}
pet2 = {"animal": "Cat", "owner": "Bob"}
pet3 = {"animal": "Parrot", "owner": "Charlie"}
pet4 = {"animal": "Rabbit", "owner": "David"}
pet5 = {"animal": "Goldfish", "owner": "Emma"}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")

### 6-9. Favorite Places: 
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'Alice': ['Paris', 'Kyoto'],
    'Bob': ['New York'],
    'Charlie': ['Sydney', 'London', 'Tokyo']
}

for person, place in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in place:
        print(f"- {place}")

### 6-10. Favorite Numbers: 
# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers

favorite_numbers = {
    "Monkey D. Luffy": [56, 41], 
    "Roronora Zoro": [3], 
    "Nami": [10, 13, 54], 
    "Usopp": [800], 
    "Sanji": [77, 88]
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in number:
        print(f"- {number}")

### 6-11. Cities: 
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8982000,
        'fact': 'London is the capital city of England.'
    },
    'New York City': {
        'country': 'United States',
        'population': 8398748,
        'fact': 'New York City is known as "The Big Apple".'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    for key, value in info.items():
        print(f"\t{key.capitalize()}: {value}")
    print() 

### 6-12. Extensions: 
# We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output

cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
        'landmarks': ['Tokyo Tower', 'Senso-ji Temple', 'Shibuya Crossing']
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8982000,
        'fact': 'London is the capital city of England.',
        'landmarks': ['Big Ben', 'Buckingham Palace', 'Tower of London']
    },
    'New York City': {
        'country': 'United States',
        'population': 8398748,
        'fact': 'New York City is known as "The Big Apple".',
        'landmarks': ['Statue of Liberty', 'Empire State Building', 'Central Park']
    },
    'Paris': {
        'country': 'France',
        'population': 2140526,
        'fact': 'Paris is known as the "City of Love".',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral']
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")
    print("\tLandmarks:")
    for landmark in info["landmarks"]:
            print(f"\t\t- {landmark}")
