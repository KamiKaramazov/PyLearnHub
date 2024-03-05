import random

def guess_number(x):
    # Generate a random number between 0 and x
    random_number = random.randint(0, x)
    
    # Initialize a variable to store the user's guess
    user_guess = -1  # Set to an invalid value initially
    
    # Keep looping until the user's guess matches the random number
    while user_guess != random_number:
        # Get the user's guess as an integer
        user_guess = int(input(f"Guess a number between 0 and {x}: "))
        
        # Compare the user's guess with the random number
        if user_guess < random_number:
            print("Your guess is too low!")
        elif user_guess > random_number:
            print("Your guess is too high!")

    # The loop exits when the user's guess matches the random number
    print(f"Yes, you've found the number: {random_number}!")

# Call the function to start the game with a range up to 10
guess_number(10)
