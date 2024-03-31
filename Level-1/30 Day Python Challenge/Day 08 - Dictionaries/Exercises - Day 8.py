### Exercises: Day 8
# Create an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary

dogs = [
    {"name": "Fido", "color": "Brown", "breed": "Labrador", "legs": 4, "age": 3},
    {"name": "Buddy", "color": "Black", "breed": "German Shepherd", "legs": 4, "age": 2},
    {"name": "Max", "color": "Golden", "breed": "Golden Retriever", "legs": 4, "age": 5},
    {"name": "Rocky", "color": "White", "breed": "Siberian Husky", "legs": 4, "age": 4}
]

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

skills = student["skills"]
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills

new_skills = ["Art", "Music"]
student["skills"].extend(new_skills)

print(student["skills"])

# Get the dictionary keys as a list

keys_list = list(student.keys())
print(keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

# Change the dictionary to a list of tuples using items() method
dict_to_tuples = list(student.items())
print(dict_to_tuples)

# Delete one of the items in the dictionary
# Let's say you want to delete the "marital_status" key
del student["marital_status"]
print(student)

# Delete one of the dictionaries
del student
