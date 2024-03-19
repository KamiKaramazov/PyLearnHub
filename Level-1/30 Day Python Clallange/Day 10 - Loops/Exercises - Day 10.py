### Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.

i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop, do the same using while loop.

i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""  #
  ##
  ###
  ####
  #####
  ######
  #######"""

i = "#"
len = 1

while len <= 7:
    print(i)
    i += "#"
    len += 1

# Use nested loops to create the following:
"""# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #"""

for i in range(7): 
    for j in range(7):  
        print('#', end="")  
    print()  

# Print the following pattern:
"""0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""

i = 0

while i <= 10:
    print(f"{i} x {i} = {i * i}")
    i += 1

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in list:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers

for number in range(0, 101, 2):
    print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for number in range(0, 101, 3):
    print(number)

### Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""The sum of all numbers is 5050."""

total = 0

for number in range(101):
    total += number
print(f"The sum of all numbers is {total}.")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

even_sum = 0
odd_sum = 0

for number in range(101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

### Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

land_countries = [country for country in countries if "land" in country.lower()]

for country in land_countries:
    print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruit_list = ['banana', 'orange', 'mango', 'lemon']

reverse_list = []

for i in range(len(fruit_list) - 1, -1, -1):
    reverse_list.append(fruit_list[i])

print(reverse_list)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

import countries_data

# Extracting all languages from the data
all_languages = []
for country in countries_data.country_info:
    for language in country['languages']:
        all_languages.append(language)

# Total number of languages
total_languages = len(set(all_languages))
print("Total number of languages:", total_languages)

# Counting the occurrences of each language
language_count = {}
for language in all_languages:
    if language in language_count:
        language_count[language] += 1
    else:
        language_count[language] = 1

# Finding the ten most spoken languages
most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count} countries")

# Sorting countries by population
countries_sorted_by_population = sorted(countries_data.country_info, key=lambda x: x['population'], reverse=True)

# Finding the ten most populated countries
most_populated_countries = countries_sorted_by_population[:10]
print("\nTen most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']} people")

