# Exercises: Level 1
### Writ a function which generates a six digit/character random_user_id.
"""  
print(random_user_id());
'1ee33d
'"""

import random

def random_user_id():

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    letters_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    letters_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                        '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', 
                        ']', '^', '_', '`', '{', '|', '}', '~']

    all_characters = numbers + letters_lowercase + letters_uppercase + special_characters

    user_id = "".join(str(random.choice(all_characters)) for _ in range(6))
    return user_id

print(random_user_id())

### Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
"""

import random

def user_id_gen_by_user():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                        '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', 
                        ']', '^', '_', '`', '{', '|', '}', '~']

    all_characters = numbers + letters_lowercase + letters_uppercase + special_characters

    user_input = int(input("Enter the number of characters: ")) 
    user_ids_count = int(input("Enter the number of IDs to generate: ")) 

    user_ids = [] 

    for _ in range(user_ids_count):
        user_id = "".join(str(random.choice(all_characters)) for _ in range(user_input))
        user_ids.append(user_id) 

    return user_ids

print(user_id_gen_by_user())

### Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""

import random

def rgb_color_gen():
    color = (f"rgb({random.randint(0, 256)},{random.randint(0, 256)},{random.randint(0, 256)})")
    return color

print(rgb_color_gen())

# Exercises: Level 2
### Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

import random

def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

### Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
        colors.append(color)
    return colors

### Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type"


print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

# Exercises: Level 3
### Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(lst):
    shuffled_lst = lst[:]  
    random.shuffle(shuffled_lst)  
    return shuffled_lst

### Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def seven_unique_random_numbers():
    return random.sample(range(10), 7)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle_list(my_list)) 
print(seven_unique_random_numbers()) 

