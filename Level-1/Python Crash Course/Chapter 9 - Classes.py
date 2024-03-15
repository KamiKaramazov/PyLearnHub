### 9-1. Restaurant: 
# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

my_restaurant = Restaurant("KFC", "Chicken")
print("Restaurant Name:", my_restaurant.restaurant_name)
print("Cuisine Type:", my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

### 9-2. Three Restaurants: 
# Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant1 = Restaurant("McDonald's", "Fast Food")
restaurant2 = Restaurant("Olive Garden", "Italian")
restaurant3 = Restaurant("Sushi House", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

### 9-3. Users: 
# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"User information:\nFirst Name: {self.first_name}\nLast Name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome to the board, {self.first_name} {self.last_name}!")

user1 = User("Monkey D.", "Luffy")
user2 = User("Roronoa", "Zoro")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

### 9-4. Number Served: 
# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

    def display_number_served(self):
        print(f"Number served: {self.number_served}")

my_restaurant = Restaurant("KFC", "Chicken")
print("Restaurant Name:", my_restaurant.restaurant_name)
print("Cuisine Type:", my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.display_number_served()

my_restaurant.set_number_served(50)
my_restaurant.display_number_served()

my_restaurant.increment_number_served(30)
my_restaurant.display_number_served()

### 9-5. Login Attempts: 
# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User information:\nFirst Name: {self.first_name}\nLast Name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome to the board, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Monkey D.", "Luffy")
user2 = User("Roronoa", "Zoro")

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print("Login attempts:", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts after reset:", user1.login_attempts)
user2.describe_user()
user2.greet_user()

### 9-6. Ice Cream Stand: 
# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)

my_ice_cream_stand = IceCreamStand("Ice Delight", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])

my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.describe_flavors()
my_ice_cream_stand.open_restaurant()

### 9-7. Admin: 
# An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"User information:\nFirst Name: {self.first_name}\nLast Name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome to the board, {self.first_name} {self.last_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


get_admin = Admin("Monkey D.", "Luffy", ["can add post", "can delete post", "can ban user"])
get_admin.show_privileges()

### 9-8. Privileges: 
# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

my_admin = Admin("Monkey D.", "Luffy")
my_admin.privileges.show_privileges()

### 9-9. Battery Upgrade: 
# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
# You should see an increase in the car’s range.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

### 9-13. Dice: 
# Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

import random

class Die():
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)

six_side_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_side_die.roll_die())

ten_side_die = Die(10)
print("Rolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_side_die.roll_die())

twenty_sided_die = Die(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die())

### 9-14. Lottery: 
# Make a list or tuple containing a series of 10 numbers and five letters. 
# Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.
import random

mixed_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

class Lottery:
    def __init__(self, mixed_data):
        self.mixed_data = mixed_data

    def random_choices(self):
        return random.sample(self.mixed_data, 4)
        
lottery_instance = Lottery(mixed_data)
winners = lottery_instance.random_choices()
print("Winning ticket numbers or letters:", winners)
print("Any ticket matching these four numbers or letters wins a prize!")

### 9-15. Lottery Analysis: 
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. 
# Print a message reporting how many times the loop had to run to give you a winning ticket.

import random

my_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
while True:
    count += 1
    if random.choice(my_ticket) == random.randint(1, 10):
        print("You won! It took", count, f"tries to found {random.choice(my_ticket)}.")
        break

                                                ############ More Examples ############

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"

    def borrowed(self):
        if self.status == "available":
            self.status = "borrowed"
            print(f"The book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"The book '{self.title}' is currently not available for borrowing.")
    
    def returned(self):
        if self.status == "borrowed":
            self.status = "available"
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' has already been returned or is available.")

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book1.borrowed() 
book1.returned() 