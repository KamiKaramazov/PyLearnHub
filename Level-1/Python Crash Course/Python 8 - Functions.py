### 8-1. Message: 
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
# Call the function, and make sure the message displays correctly.

def display_message():
    print("I can use functions!")

display_message()

### 8-2. Favorite Book: 
# Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is Alice in Wonderland. 
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

### 8-3. T-Shirt: 
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"Size of this shirt is {size}.")
    print(f"{message}.")

make_shirt("L","Your shirt is ready")

### 8-4. Large Shirts: 
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love Python"):
    print(f"{size.capitalize()} shirt is ready with message: {message}")

make_shirt()
make_shirt("medium")
make_shirt("small", "Python is awesome!")

### 8-5. Cities: 
# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city = "Reykjavik", country = "Iceland"):
    print(f"{city} is in {country}.")

describe_city()
describe_city("Tokyo", "Japan")
describe_city("Paris", "French")
describe_city("Cairo", "Egypt")

### 8-6. City Names: 
# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))
print(city_country("Cairo", "Egypt"))

### 8-7. Album: 
# Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_name, num_songs=None):
    album = {"artist": artist_name, "album": album_name}
    if num_songs:
        album["num_songs"] = num_songs
    return album

album1 = make_album("Taylor Swift", "Fearless", 13)
album2 = make_album("Ed Sheeran", "÷ (Divide)", 16)
album3 = make_album("Beyoncé", "Lemonade")

print(album1)
print(album2)
print(album3)

### 8-8. User Albums: 
# Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_name, num_songs=None):
    album = {"artist": artist_name, "album": album_name}
    if num_songs:
        album["num_songs"] = num_songs
    return album

while True:
    print("\nEnter 'quit' or 'exit' to end the program.")
    artist = input("Enter the artist name: ")
    if artist.lower() == 'quit' or artist.lower() == 'exit':
        break
    album = input("Enter the album name: ")
    if album.lower() == 'quit' or album.lower() == 'exit':
        break
    songs = input("Enter the number of songs (press enter to skip): ")
    if songs.lower() == 'quit' or songs.lower() == 'exit':
        break
    if songs:
        album_dict = make_album(artist, album, songs)
    else:
        album_dict = make_album(artist, album)
    print(album_dict)

### 8-9. Messages: 
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

text_messages = [
    "Hello, how are you?",
    "Don't forget to buy milk!",
    "Meeting at 3 PM today.",
    "Happy birthday!",
    "Just checking in.",
    "See you soon!",
    "Have a great day!",
    "Remember to call mom.",
    "Congratulations!",
    "You're awesome!"
]

show_messages(text_messages)

### 8-10. Sending Messages: 
# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)  
        print(f"Sending message: {message}")
        sent_messages.append(message)

text_messages = [
    "Hello, how are you?",
    "Don't forget to buy milk!",
    "Meeting at 3 PM today.",
    "Happy birthday!",
    "Just checking in.",
    "See you soon!",
    "Have a great day!",
    "Remember to call mom.",
    "Congratulations!",
    "You're awesome!"
]

sent_messages = []
send_messages(text_messages, sent_messages)

print("\nSent Messages:")
show_messages(sent_messages)
print("\nRemaining Messages:")
show_messages(text_messages)

### 8-11. Archived Messages: 
# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)  
        print(f"Sending message: {message}")
        sent_messages.append(message)

text_messages = [
    "Hello, how are you?",
    "Don't forget to buy milk!",
    "Meeting at 3 PM today.",
    "Happy birthday!",
    "Just checking in.",
    "See you soon!",
    "Have a great day!",
    "Remember to call mom.",
    "Congratulations!",
    "You're awesome!"
]

sent_messages = []
send_messages(text_messages.copy(), sent_messages)

print("\nSent Messages:")
show_messages(sent_messages)
print("\nRemaining Messages:")
show_messages(text_messages)

### 8-12. Sandwiches: 
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def make_sandwich(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'bacon', 'tomato', 'mayonnaise')
make_sandwich('peanut butter', 'jelly')

### 8-13. User Profile: 
# Start with a copy of user_profile.py from page 149. 
# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you

def build_profile(first_name, last_name, **additional_info):
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(additional_info)
    return profile

my_profile = build_profile('John', 'Doe', age=30, occupation='Software Engineer', city='New York')
print(my_profile)

### 8-14. Cars: 
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(car_info)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

### 8-15. Printing Models: 
# Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

def print_models(models):
    for model in models:
        print(f"Printing {model}")

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)


                                                ############ More Examples ############

# Write a function called calculate_average that takes a list of numbers as input and returns the average of those numbers.

from statistics import mean 

def calculate_average(*numbers):
    average = str(mean(numbers))
    return average
    
numbers = []

print("\nEnter 'quit' or 'exit' to end the program.")

while True:
        user_input = input("Please enter a number: ")
        if user_input.lower() in ["quit", "exit"]:
              break
        numbers.append(float(user_input))

average = calculate_average(*numbers)
print(f"The average is: {average}")

# Create a function called is_prime that takes an integer as input and returns True if the number is prime, and False otherwise.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))  
print(is_prime(10))

# Write a function called reverse_string that takes a string as input and returns the reverse of that string.

def reverse_string(string):
    reverse = string[::-1]
    return reverse

print("\nEnter 'quit' or 'exit' to end the program.")

while True:
    user_input = input("Enter your string: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    reversed_string = reverse_string(user_input)
    print("Reversed string:", reversed_string)

# Create a function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(string):
    count = 0 
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
    
input_str = input("Enter your input: ")
result = count_vowels(input_str)
print("Number of vowels:", result)

# Write a function called find_max that takes a list of numbers as input and returns the largest number in the list.

def find_max(numbers):
    if not numbers:
        return None  
    return max(numbers)

while True:
    print("\nEnter 'quit' or 'exit' to end the program.")
    user_input = input("Enter numbers (separated by spaces): ")
    if user_input.lower() == 'quit' or user_input.lower() == 'exit':
        break
    
    try:
        num_list = [int(num) for num in user_input.split()]
        print("Max number is:", find_max(num_list))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Create a function called capitalize_words that takes a string as input and returns the same string with each word capitalized.

def capitalize_words(words):
    return words.title()

while True:
    print("\nEnter 'quit' or 'exit' to end the program.")
    user_input = input("Enter words: ")
    if user_input.lower() == 'quit' or user_input.lower() == 'exit':
        break
    capitalized_input = capitalize_words(user_input)
    print("Capitalized words:", capitalized_input)

