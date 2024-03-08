### 2-3. Personal Message: 
# Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?"
name = input("Enter your name: ")
print(f"Hello {name.title()}, would you like to learn some Python today?")

# 2-4. Name Cases: 
# Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = input("Enter your name: ")
options = input("Select one of the following options:\n1. Lowercase\n2. Uppercase\n3. Titlecase\n")

def print_name(name, options):
    if options == "1":
        return name.lower()
    elif options == "2":
        return name.upper()
    elif options == "3":
        return name.title()
    else:
        return "Invalid option selected."

formatted_name = print_name(name, options)
print(f"Hello {formatted_name}, would you like to learn some Python today?")

### 2-5. Famous Quote: 
# Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print("Albert Einstein once said, “A person who never made a \nmistake never tried anything new.")

### 2-6. Famous Quote 2: 
# Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Albert Einstein"
print(f"{famous_person} once said, “A person who never made a \nmistake never tried anything new.")

### Stripping Names: 
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name_with_whitespace = input("Enter your name (including spaces): ")
title_name = name_with_whitespace.title()
print("Original Name:", title_name)
print("Using lstrip():", title_name.lstrip())      
print("Using rstrip():", title_name.rstrip())
print("Using strip():", title_name.strip())

### 2-8. Number Eight: 
# Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. Your output should simply be four lines with the number 8 appearing once on each line.
print(5 + 3)
print(16 - 8)
print(4 * 2)
print(16 / 2)