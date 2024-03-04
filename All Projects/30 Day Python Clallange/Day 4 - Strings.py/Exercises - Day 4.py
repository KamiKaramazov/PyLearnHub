### Exercises: Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
formatted = f"{a} {b} {c} {d}"
print(formatted)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = "Coding"
b = "For"
c = "All"
single_string = f"{a} {b} {c}"
print(single_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(str(company)))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.swapcase())
print(company.title())

# Cut(slice) out the first word of Coding For All string.
slice_company= company.split(" ", 1)[1]
print(slice_company)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
index = company.find("Coding")
try:
    index = company.index("Coding")
    print("Coding found at index:", index)
except ValueError:
    print("Coding not found using index() method")
print(index)

# Replace the word coding in the string 'Coding For All' to Python.
modify = company.replace("Coding", "Python")
print(modify)

# Change "Python for Everyone" to "Python for All" using the replace method
change = company.replace("Python for Everyone", "Python for All")
print(change)

# Split the string 'Coding For All' using space as the separator
split =company.split(" ")
print(split)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
more_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_more_company = more_company.split(", ")
print(split_more_company)

# What is the character at index 0 in the string "Coding For All"
string = "Coding For All"
character_at_index_0 = string[0]
print(character_at_index_0) 

# What is the last index of the string "Coding For All
string = "Coding For All"
last_index = len(string) - 1
print(last_index)  

# What character is at index 10 in the string "Coding For All"
string = "Coding For All"
character_at_index_10 = string[10]
print(character_at_index_10)  

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
acronym = ''.join(word[0].upper() for word in name.split())
print(acronym)  

# Create an acronym or an abbreviation for the name 'Coding For All'
name = "Coding For All"
acronym = ''.join(word[0].upper() for word in name.split())
print(acronym)  

# Use index to determine the position of the first occurrence of 'C' in "Coding For All"
string = "Coding For All"
first_occurrence_of_C = string.index('C')
print(first_occurrence_of_C)  

# Use index to determine the position of the first occurrence of 'F' in "Coding For All"
string = "Coding For All"
first_occurrence_of_F = string.index('F')
print(first_occurrence_of_F)  

# Use rfind to determine the position of the last occurrence of 'l' in "Coding For All People"
string = "Coding For All People"
last_occurrence_of_l = string.rfind('l')
print(last_occurrence_of_l)  

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence_of_because = sentence.find('because')
print(first_occurrence_of_because)  

# Use rindex to find the position of the last occurrence of the word 'because' in the following sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
last_occurrence_of_because = sentence.rindex('because')
print(last_occurrence_of_because)  #

# Slice out the phrase 'because because because' in the following sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[31:31 + len('because because because')]
print(phrase)  

# Find the position of the first occurrence of the word 'because' in the following sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence_of_because = sentence.index('because')
print(first_occurrence_of_because) 

# Slice out the phrase 'because because because' in the following sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[sentence.index('because'):sentence.rindex('because') + len('because')]
print(phrase) 

# Does 'Coding For All' start with a substring 'Coding'
string = 'Coding For All'
starts_with_Coding = string.startswith('Coding')
print(starts_with_Coding)  

# Does 'Coding For All' end with a substring 'coding'
string = 'Coding For All'
ends_with_coding = string.endswith('coding')
print(ends_with_coding)  

# ' Coding For All ', remove the left and right trailing spaces in the given string
string = '   Coding For All      '
trimmed_string = string.strip()
print(trimmed_string)  

# Which one of the following variables return True when we use the method isidentifier()
variables = ['30DaysOfPython', 'thirty_days_of_python']
identifier = [variable.isidentifier() for variable in variables]
print(identifier) 

# The following list contains the names of some of Python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)  

# Use the new line escape sequence to separate the following sentences
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)

# Use a tab escape sequence to write the following lines
lines = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(lines)

# Use the string formatting method to display the following
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods
# Mathematical operations
addition = 8 + 6
subtraction = 8 - 6
multiplication = 8 * 6
division = 8 / 6
modulo = 8 % 6
floor_division = 8 // 6
exponentiation = 8 ** 6

# Display the results using string formatting
print(f"8 + 6 = {addition}")
print(f"8 - 6 = {subtraction}")
print(f"8 * 6 = {multiplication}")
print(f"8 / 6 = {division}")
print(f"8 % 6 = {modulo}")
print(f"8 // 6 = {floor_division}")
print(f"8 ** 6 = {exponentiation}")