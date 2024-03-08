### 3-1. Names: 
# Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Sanji", "Tony Tony Chopper", "Nico Robin", "Franky", "Brook", "Jimbei"]
for characters in names:
    print(characters)

### 3-2. Greetings: 
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
for characters in names:
    print(f"Hello, {characters}! It's great to see you.")

### 3-3. Your Own List: 
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
vehicles = ["Tesla Model S", "Jeep Wrangler", "BMW M3", "Toyota Prius"]
for characters in vehicles:
    print(f"I would like to own a {characters}.")

### 3-4. Guest List: 
# If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
invite = ["Monkey D. Luffy", "Roronoa Zoro"]
your_name = input("Enter your name:").strip()

def check_number(your_name):
    if any(character.isdigit() for character in your_name):
        print("Please enter a name without any numbers.")
    else:
        for person in invite:
            print(f"Dear {person},\nYou are cordially invited to a delightful dinner at my place. Let's share great conversations and good food!\nSincerely,\n{your_name.title()}")

check_number(your_name)

### 3-5. Changing Guest List: 
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it. • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. • Print a second set of invitation messages, one for each person who is still in your list.
import random
invite = ["Monkey D. Luffy", "Roronoa Zoro"]
chosen_invite = random.choice(invite)
your_name = input("Enter your name:").strip()

def check_number(your_name):
    if any(character.isdigit() for character in your_name):
        print("Please enter a name without any numbers.")
    elif chosen_invite in invite:
        print(f"Dear {chosen_invite},\nYou are cordially invited to a delightful dinner at my place. Let's share great conversations and good food!\nSincerely,\n{your_name.title()}")
        invite.remove(chosen_invite)
        print(f"Unfortunately, {chosen_invite} cannot make it. However, you are still invited!")
check_number(your_name)

new_invite = input("Chose one of the visitor: \n1.Nami \n2.Usopp \n3.Sanji \n4.Tony Tony Chopper \n5.Nico Robin \n6.Franky \n7.Brook \n8.Jimbei\n" )
update = new_invite.strip()
def handle_new_invite():
    if update.isdigit():
        new_invite_num = int(update)
        if new_invite_num == 1:
            print("New invite for Nami!")
        elif new_invite_num == 2:
            print("New invite for Usopp!")
        elif new_invite_num == 3:
            print("New invite for Sanji!")
        elif new_invite_num == 4:
            print("New invite for Tony Tony Chopper!")
        elif new_invite_num == 5:
            print("New invite for Nico Robin!")
        elif new_invite_num == 6:
            print("New invite for Franky!")
        elif new_invite_num == 7:
            print("New invite for Brook!")
        elif new_invite_num == 8:
            print("New invite for Jimbei!")
        else:
            print("Invalid option selected.")
    else:
        print("Please enter a valid number.")

handle_new_invite()

### 3-6. More Guests: 
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table. • Use insert() to add one new guest to the beginning of your list. • Use insert() to add one new guest to the middle of your list. • Use append() to add one new guest to the end of your list. • Print a new set of invitation messages, one for each person in your list.
import random

invite = ["Monkey D. Luffy", "Roronoa Zoro"]
chosen_invite = random.choice(invite)
your_name = input("Enter your name: ").strip()

def check_number(your_name):
    if any(character.isdigit() for character in your_name):
        print("Please enter a name without any numbers.")
    elif chosen_invite in invite:
        print(f"Dear {chosen_invite},\nYou are cordially invited to a delightful dinner at my place. Let's share great conversations and good food!\nSincerely,\n{your_name.title()}")
        invite.remove(chosen_invite)
        print(f"Unfortunately, {chosen_invite} cannot make it. However, you are still invited!")

check_number(your_name)

def handle_new_invite():
    print("\nAs you have more space available at the dinner table, you can choose additional guests to invite.")
    print("Choose one or more visitors by entering their numbers separated by commas:")
    print("1. Nami\n2. Usopp\n3. Sanji\n4. Tony Tony Chopper\n5. Nico Robin\n6. Franky\n7. Brook\n8. Jimbei")
    new_invite = input("Enter numbers: ")
    selected_visitors = []
    for num in new_invite.split(","):
        num = int(num.strip())
        if num >= 1 and num <= 8:
            selected_visitors.append(num)
        else:
            print(f"Invalid option: {num}")

    if selected_visitors:
        print("\nNew invites:")
        for num in selected_visitors:
            if num == 1:
                print("Nami")
            elif num == 2:
                print("Usopp")
            elif num == 3:
                print("Sanji")
            elif num == 4:
                print("Tony Tony Chopper")
            elif num == 5:
                print("Nico Robin")
            elif num == 6:
                print("Franky")
            elif num == 7:
                print("Brook")
            elif num == 8:
                print("Jimbei")

handle_new_invite()




