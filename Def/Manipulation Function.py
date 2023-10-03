##String Manipulation Function
#Write a Python function called reverse_and_uppercase that takes a string as an argument, reverses the string, and converts it to uppercase. The function should return the modified string. Test your function with different input strings.

word = input("Please enter the word: ")
choice = input("Please select reverse 'r', uppercase 'u' or lowercase 'l': ")

def reverse(input_string):
    return input_string[::-1]

def uppercase(input_string):
    return input_string.upper()

def lowercase(input_string):
    return input_string.lower()

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