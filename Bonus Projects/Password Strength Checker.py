##Password Strength Checker Function
#Write a Python function called password_strength that takes a password string as input and checks its strength. The function should return a message indicating whether the password is weak, moderate, or strong based on criteria like length, use of uppercase and lowercase letters, numbers, and special characters.

# Prompt the user for a password
user_pass = input("Please enter your password: ")

def is_strong_password(user_pass):
    # Minimum password length
    min_length = 8

    # Check length
    if len(user_pass) < min_length:
        return f"Weak: Password is too short. Add {min_length - len(user_pass)} more characters."

    # Check for an uppercase letter
    if not any(char.isupper() for char in user_pass):
        return "Weak: Password must contain at least one uppercase letter."

    # Check for a lowercase letter
    if not any(char.islower() for char in user_pass):
        return "Weak: Password must contain at least one lowercase letter."

    # Check for a digit
    if not any(char.isdigit() for char in user_pass):
        return "Weak: Password must contain at least one digit."

    # Check for a special character
    if not any(char in "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/~" for char in user_pass):
        return "Weak: Password must contain at least one special character."

    # If all criteria are met, the password is strong
    return "Strong: Password meets all criteria."

# Call the function to check password strength
result = is_strong_password(user_pass)

# Display the result
print(result)
