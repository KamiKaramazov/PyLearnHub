### 4-1. Pizzas: 
# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas_list = ["Pizzazz Pizzeria", "Bella Napoli Bites", "Rustica Pizza Kitchen"]
for pizza in pizzas_list:
    print(f"I like {pizza}!")

print("I really love pizza!")

### 4-2. Animals: 
# Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!

animal_list = ["Lion", "Wolves", "Elephants"]
for animal in animal_list:
    if animal == "Lion":
        print(f"A {animal} is known as the king of the jungle.")
    elif animal == "Wolves":
        print(f"{animal} are highly social animals that live in packs.")
    else:
        print(f"An {animal} is known for its strong social bonds and intelligence.")

print("The common characteristic among these animals is their social behavior and reliance on group cooperation for survival and reproduction.")

### 4-3. Counting to Twenty: 
# Use a for loop to print the numbers from 1 to 20, inclusive.

for value in range(1, 21):
    print(value)

### 4-4. One Million:
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
    
one_mill = list(range(1, 1000001))
print(one_mill)

for value in range(1,1000001):
    print(value)

### 4-5. Summing a Million: 
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers

numbers = list(range(1, 1000001))

print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of all numbers:", sum(numbers))

### 4-6. Odd Numbers: 
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

for number in range(1, 21, 1):
    print(number)

### 4-7. Threes: 
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

for number in range(3,31,3):
    print(number)

### 4-8. Cubes: 
# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cube = []
for number in range(1,11):
    cube = number ** 3
    print(cube)

### 4-9. Cube Comprehension: 
# Use a list comprehension to generate a list of the first 10 cubes.

cube = [number ** 3 for number in range(1,11)]
print(cube)

### 4-10. Slices: 
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

pizzas_list = ["Pizzazz Pizzeria", "Bella Napoli Bites", "Rustica Pizza Kitchen"]

def first_three():
        print("The first three items in the list are:")
        for pizza in pizzas_list[:3]:
            print(pizza)

first_three()

def middle_pizza():
        print("Three items from the middle of the list are:")
        middle_index = len(pizzas_list) // 2
        middle_slice = pizzas_list[middle_index - 1: middle_index + 2]
        print(middle_slice)

middle_pizza()

def last_pizza():
        print("The last three items in the list are:")
        for pizza in pizzas_list[-3:]:
            print(pizza)

last_pizza()

### 4-11. My Pizzas, Your Pizzas: 
# Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

# Original list of pizzas
my_pizzas = ["Pizzazz Pizzeria", "Bella Napoli Bites", "Rustica Pizza Kitchen"]

friend_pizzas = my_pizzas.copy()

my_pizzas.append("Margherita Pizza")

friend_pizzas.append("Pepperoni Pizza")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

### 4-13. Buffet: 
# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the change.
# • The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

from os import replace


simple_foods = ("apple", "banana", "bread", "cheese", "rice")

def each_food():
    for food in simple_foods:
        print(food)

each_food()

try:
    simple_foods[0] = "orange"
except TypeError as e:
    print("Error:", e)

revised_menu = ("orange", "mango", "bread", "cheese", "spaghetti")

print("Revised menu:")
for food in revised_menu:
    print(food)

