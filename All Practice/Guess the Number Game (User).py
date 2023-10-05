import random

# Define a function for the computer to guess the user's number.
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    
    # Start a loop until the computer's guess is correct (feedback is "c").
    while feedback != "c":
        # Check if the range is valid.
        if low > high:
            print("Invalid range. Please enter a valid number.")
            return  # Exit the function if the range is invalid.
        
        # Generate a random guess within the current range.
        guess = random.randint(low, high)
        
        # Ask the user for feedback on the guess (too high, too low, or correct).
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        # Update the range based on the user's feedback.
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    # Print a message when the computer correctly guesses the user's number.
    print(f"The computer guessed your number, {guess}, correctly!")

# Get the user's chosen number as input.
user_number = int(input("Pick a number: "))

# Call the computer_guess function with the user's chosen number.
computer_guess(user_number)
