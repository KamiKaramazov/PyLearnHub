# Import the Random module
import random

# Store story elements in different lists
time = ["A very long time ago", "Yesterday", "Before you were born", "In the future", "Before Thanos came"]
who = ["Shazam", "Iron Man", "Batman", "Superman", "Captain America"]
where = ["Arkham Asylum", "Gotham City", "Stark Tower", "Bat Cave", "Avengers HQ"]
what = ["to eat too much cake", "to fight for justice", "to steal ice cream", "to dance"]

# Create a story by selecting random elements from the lists
story = f"{random.choice(time)}, {random.choice(who)} went to {random.choice(where)} {random.choice(what)}."

# Print the story
print(story)
