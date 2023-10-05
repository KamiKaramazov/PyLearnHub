import random

# Define a function to play the Rock-Paper-Scissors game
def play():
    # Get user's choice
    user = input("Please select one of the choices.\nRock for 'r' or Paper 'p' or Scissors 's': ").lower()
    
    # Generate a random choice for the computer
    computer = random.choice(['r', 'p', 's'])

    # Check for a tie
    if user == computer:
        return "It's a tie!"

    # Check if the user wins
    if is_win(user, computer):
        return "You win!"

    # If neither tie nor win, user lost
    return "You lost!"

# Define a function to determine the winner
def is_win(player, opponent):
    # Check for winning conditions
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

# Call the play function and print the result
print(play())
