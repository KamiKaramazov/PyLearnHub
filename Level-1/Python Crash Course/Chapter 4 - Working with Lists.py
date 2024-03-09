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