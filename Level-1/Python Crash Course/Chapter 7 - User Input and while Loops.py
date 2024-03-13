### 7-1. Rental Car: 
# Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

car = input("What kind of rental car they would like?\n")

print(f"Let me see if I can find you a {car.title()}.")

### 7-2. Restaurant Seating: 
# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

count_people = input("How many people are in their dinner group?\n")

print(f"They'll have to wait for {count_people} table.\nOtherwise, report that their table is ready")

### 7-3. Multiples of Ten: 
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = int(input("Give me a number: "))

if number % 10 == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} is not multiple of 10.")

### 7-4. Pizza Toppings: 
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

pizzas = []

while True:
    add_pizza = input("Enter a topping for your pizza (Enter 'quit' when you are finished): ")
    if add_pizza.lower() == 'quit':
        break
    print(f"You'll add {add_pizza} topping to your pizza.")
    pizzas.append(add_pizza)

print("Your pizza toppings:")
for pizza in pizzas:
    print(pizza)

### 7-5. Movie Tickets: 
# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

age = int(input("Please enter your age: "))

if age < 3:
    print("Your ticket is free!")
elif 3 <= age <= 12:    
    print("Ticket price is $10.")
else:
    print("Ticket price is $15.") 

### 7-6. Three Exits: 
# Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")
    
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    
    if age < 12:
        print("This movie is suitable for ages 12 and above!")
    elif 12 <= age <= 16:    
        print("Ticket price is $10.")
    else:
        print("Ticket price is $15.")

### 7-7. Infinity: 
# Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

infinite_loop = "This loop is infinite!"

while True:
    print(infinite_loop)
    break # delete this for infinite loop

### 7-8. Deli: 
# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["Ham and Cheese", "Turkey Club", "BLT", "Grilled Chicken", "Vegetarian", "Tuna Salad", "Pastrami"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your tuna {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nThese are the finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Ham and Cheese", "Turkey Club", "BLT", "Grilled Chicken", "Vegetarian", "Tuna Salad", "Pastrami", "Pastrami", "Pastrami"]
finished_sandwiches = []

print("Sorry, we've run out of Pastrami.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThese are the finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

### 7-10. Dream Vacation: 
# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll

dream_vacation = []

while True:
    place = input("If you could visit one place in the world, where would you go? (If you wanna exit enter 'quit' or 'exit')\n")
    if place.lower() == 'quit' or place.lower() == 'exit':
        break
    else:
        dream_vacation.append(place)
        print(f"Dream vacation list:\n{place}")

print("Dream vacation list:")
for place in dream_vacation:
    print(place)

