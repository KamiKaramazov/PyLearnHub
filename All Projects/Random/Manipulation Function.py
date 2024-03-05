##String Manipulation Function
#Write a Python function called reverse_and_uppercase that takes a string as an argument, reverses the string, and converts it to uppercase. The function should return the modified string. Test your function with different input strings.

# Get user input for a word
word = input("Please enter the word: ")
# Get user choice for operation: reverse 'r', uppercase 'u', or lowercase 'l'
choice = input("Please select reverse 'r', uppercase 'u' or lowercase 'l': ")

# Define a function that reverses a string
def reverse(input_string):
    return input_string[::-1]

# Define a function that converts a string to uppercase
def uppercase(input_string):
    return input_string.upper()

# Define a function that converts a string to lowercase
def lowercase(input_string):
    return input_string.lower()

# Perform the selected operation and print the result
if choice == 'r':
    result = reverse(word)
    print("Reversed:", result)
elif choice == 'u':
    result = uppercase(word)
    print("Uppercase:", result)
elif choice == 'l':
    result = lowercase(word)
    print("Lowercase:", result)
else:
    print("Invalid choice. Please select 'r', 'u', or 'l'.")