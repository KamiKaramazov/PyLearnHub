### 5-1. Conditional Tests: 
# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
# • Look closely at your results, and make sure you understand why each line evaluates to True or False.
# • Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.

console = "PS5"

print("Is the console equal to 'PS5'? I predict True.")
print(console == 'PS5')

print("\nIs the console equal to 'Xbox'? I predict False.")
print(console == 'Xbox')

print("\nIs the console not equal to 'PS4'? I predict True.")
print(console != 'PS4')

print("\nIs the console in lowercase? I predict False.")
print(console.islower())

print("\nDoes the console contain 'PS'? I predict True.")
print('PS' in console)

print("\nIs the console empty? I predict False.")
print(not console)

print("\nIs the console equal to 'ps5'? I predict False.")
print(console == 'ps5')

print("\nIs the console equal to 'Xbox' or 'PS5'? I predict True.")
print(console == 'Xbox' or console == 'PS5')

print("\nIs the console equal to 'PS5' and not equal to 'Xbox'? I predict True.")
print(console == 'PS5' and console != 'Xbox')

print("\nIs the console equal to 'Xbox' or 'PS4'? I predict False.")
print(console == 'Xbox' or console == 'PS4')

### 5-2. More Conditional Tests: 
# You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list if Statements

str1 = "hello"
str2 = "world"

print("Tests for equality and inequality with strings:")
print("Is str1 equal to 'hello'? I predict True.")
print(str1 == "hello")

print("\nIs str2 not equal to 'hello'? I predict True.")
print(str2 != "hello")

str3 = "Python"
str4 = "PYTHON"

print("\nTests using the lower() method:")
print("Is str3 equal to 'python' in lowercase? I predict True.")
print(str3.lower() == "python")

print("\nIs str4 equal to 'python' in lowercase? I predict True.")
print(str4.lower() == "python")

num1 = 10
num2 = 20

print("\nNumerical tests:")
print("Is num1 equal to 10? I predict True.")
print(num1 == 10)

print("\nIs num2 not equal to 10? I predict True.")
print(num2 != 10)

print("\nIs num1 greater than num2? I predict False.")
print(num1 > num2)

print("\nIs num1 less than or equal to num2? I predict True.")
print(num1 <= num2)

num3 = 5
num4 = 15

print("\nTests using the 'and' keyword and the 'or' keyword:")
print("Is num1 greater than 5 and num2 less than 25? I predict True.")
print(num1 > 5 and num2 < 25)

print("\nIs num3 less than 10 or num4 greater than 20? I predict True.")
print(num3 < 10 or num4 > 20)

my_list = [1, 2, 3, 4, 5]

print("\nTest whether an item is in a list:")
print("Is 3 in my_list? I predict True.")
print(3 in my_list)

print("\nTest whether an item is not in a list:")
print("Is 6 not in my_list? I predict True.")
print(6 not in my_list)

### 5-3. Alien Colors #1: 
# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = "green"

if alien_color ==  "green":
    print("Congratulations! You just shot down a green alien and earned 5 points!")
else:
    print("Congratulations! You just shot down an alien, but it was not green.")

### 5-4. Alien Colors #2: 
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# • Write one version of this program that runs the if block and another that runs the else block.

alien_color = "yellow"  

if alien_color == "green":
    print("Congratulations! You just shot down a green alien and earned 5 points!")
else:
    print("Congratulations! You just shot down an alien and earned 10 points!")

### 5-5. Alien Colors #3: 
# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = "red"

if alien_color == "green":
    print("Congratulations! You just shot down a green alien and earned 5 points!")
elif alien_color == "yellow":
        print("Congratulations! You just shot down an yellow alien and earned 10 points!")
else:
    print("Congratulations! You just shot down an red alien and earned 15 points!")

### 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

age = int(input("Please enter your age: "))

if age <= 2:
     print("You're a baby!")
elif age >= 2 and age <= 4:
     print("You're a toddler!")
elif age >= 4 and age <=13:
     print("You're a kid!")
elif age >= 13 and age <= 20:
     print("You're a teenager!")
elif age >=20 and age <= 65:
     print("You're an adult")
else:
     print("You're an elder!")

### 5-7. Favorite Fruit: 
# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ["Apple", "Banana", "Cherry", "Orange", "Strawberry"]

guess = input("Enter your favorite fruit: ").title()

if guess in favorite_fruits:
    print("You really like", guess + "s!")
else:
    print("That's not one of your favorite fruits.")

### 5-8. Hello Admin: 
# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

usernames = ["admin", "users", "Monkey D. Luffy", "Roronora Zoro", "Nami", "Usopp", "Sanji"]
name = input("What is your user name?\n")

if name == "admin":
    print("Hello admin, would you like to see a status report?")
elif name in usernames:
    print(f"Hello {name.title()}, thank you for logging in again.")
else:
    print(f"Hello {name.title()}, thank you for logging in again.")

### 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

usernames.clear()
if not usernames:
    print("We need to find some users!")

### 5-10. Checking Usernames: 
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["admin", "users", "Monkey D. Luffy", "Roronora Zoro", "Nami", "Usopp", "Sanji"]
new_users = ["Monkey D. Luffy", "Roronora Zoro", "Kami"]
add = input("What is your user name: ")
add_lower = add.lower()

for user in new_users:
    if user.lower() in current_users or user.lower() in new_users:
        print(f"Sorry, the username '{user.title()}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user.title()}' is available.")

if add_lower in current_users or add_lower in new_users:
    print(f"Sorry, the username '{add.title()}' is already taken. Please enter a new username.")
else:
    print(f"The username '{add.title()}' is available.")

### 5-11. Ordinal Numbers: 
# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

stored_numbers = list(range(1,10))

for number in stored_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")