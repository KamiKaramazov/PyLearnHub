# 3-4. Guest List: Create a list of people you'd like to invite to dinner.
# Include at least three individuals, living or deceased. Use the list to
# send each person an invitation message for the dinner.

people = ["liam", "noah", "oliver", "james", "olivia", "ava"]
invited = []
un_invited = []

for _ in range(4):
    un_invited.append(people.pop(0).title())

for person in people:
    invited.append(person.title())

print(f"{', '.join(un_invited)} are uninvited to dinner!")
print(f"{', '.join(invited)} are invited to dinner!")

