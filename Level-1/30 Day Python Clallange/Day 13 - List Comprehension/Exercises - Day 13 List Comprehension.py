# Exercises: Day 13
### Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [number for number in numbers if number <=0]
print(filtered_numbers)

### Flatten the following list of lists of lists to a one dimensional list :
"""
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_numbers = [number for sublist in list_of_lists for inner_list in sublist for  number in inner_list ]
print(flatten_numbers)

### Using list comprehension create the following list of tuples:

"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""

result = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(result)

### Flatten the following list to a new list:
"""output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print(flattened_countries)


### Change the following list to a list of dictionaries:
"""output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(dict_countries)


### Change the following list of lists to a list of concatenated strings:
"""output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]
print(concatenated_names)

### Write a lambda function which can solve a slope or y-intercept of linear functions.

linear_function = lambda x, m, c: m * x + c
slope = linear_function(3, 2, 1)
print(slope)
