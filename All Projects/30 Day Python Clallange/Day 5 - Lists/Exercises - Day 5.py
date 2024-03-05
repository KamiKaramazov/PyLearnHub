### Exercises: Level 1
# Declare a list with more than 5 items
list5 = ("A" , "B" , "C" , "D" , "E")

# Find the length of your list
print(len(list5))

# Get the first item, the middle item and the last item of the list
first_item = list5[0]
middle_item = list5[len(list5) // 2]
last_item = list5[-1]

print("First item of the list:", first_item)
print("Middle item of the list:", middle_item)
print("Last item of the list:", last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Kami" , 31 , 310 , "God" , "Universe" ]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Amazon"]

print(mixed_data_types)
print(it_companies)

# Print the number of companies in the list
print("Number of companies in the list:" , len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print(first_company)
print(middle_company)
print(last_company)

# Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Samsung")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies != "IBM":
        it_companies[i] = it_companies[i].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
for i in range(len(it_companies)):
    it_companies[i] = "#;" + it_companies[i]

print(it_companies)

# Check if a certain company exists in the it_companies list.
company_check = input("Enter the company name to check: ")
if company_check in it_companies:
    print(f"{company_check} exists in the list.")
else:
    print(f"{company_check} does not exist in the list.")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_companies = it_companies[middle_index] if len(it_companies) % 2 != 0 else it_companies[middle_index-1:middle_index+1]
print(middle_companies)

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
if len(it_companies) % 2 != 0:
    del it_companies[len(it_companies) // 2]
else:
    middle_index = len(it_companies) // 2
    del it_companies[middle_index - 1:middle_index + 1]

print(it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Insert Python and SQL after Redux in the joined list
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

### Exercises: Level 2

import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = min(sorted_ages)
max_age = max(sorted_ages)

print("Minimum age:", min_age)
print("Maximum age:", max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

print("Updated list:", ages)

# Find the median age (one middle item or two middle items divided by two)
median_age = statistics.median(ages)
print("Median age:", median_age)

# Find the average age (sum of all items divided by their number )
average_age = statistics.mean(ages)
print("Average age:", average_age)

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print("Age range:", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
average_age = statistics.mean(ages)
min_age = min(ages)
max_age = max(ages)
min_difference = abs(min_age - average_age)
max_difference = abs(max_age - average_age)
if min_difference > max_difference:
    print("Difference between min and average is greater than difference between max and average.")
elif min_difference < max_difference:
    print("Difference between max and average is greater than difference between min and average.")
else:
    print("Difference between min and average is equal to difference between max and average.")