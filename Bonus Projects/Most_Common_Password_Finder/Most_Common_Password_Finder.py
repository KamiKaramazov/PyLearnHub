from collections import Counter

# Function to read the file and extract passwords
def extract_passwords(file_path):
    passwords = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    passwords.append(parts[1].strip())  # Strip extra spaces from the password
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while reading the file:", e)
    return passwords

# Function to find the most common password
def most_common_password(passwords):
    password_counts = Counter(passwords)
    most_common = password_counts.most_common(1)
    return most_common[0][0] if most_common else None

# Main function
def main():
    file_path = "Bonus Projects/Most_Common_Password_Finder/Passwords_data.txt"  # Change this to your file path
    passwords = extract_passwords(file_path)
    if passwords:
        most_common = most_common_password(passwords)
        if most_common:
            print(f"The most commonly used password is: {most_common}")
        else:
            print("No passwords found in the file.")
    else:
        print("No passwords found in the file.")

if __name__ == "__main__":
    main()