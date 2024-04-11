from pwn import *
import sys
import hashlib

if len(sys.argv) != 2:  
    # Check if the number of command-line arguments is not equal to 2.
    # This condition expects two arguments: the program name itself and the sha256 sum.
    print("Invalid arguments!")
    print(">> {} <sha256 sum>".format((sys.argv[0])))
    exit()

wanted_hash = sys.argv[1]  
# Extract the second command-line argument, which is the sha256 hash provided by the user.

password_file = "rockyou.txt"  
# Set the filename of the password file to be used for cracking.

attempts = 0  
# Initialize a counter to keep track of the number of attempts made to crack the hash.

with log.progress('Attempting to crack: {}!\n'.format(wanted_hash)) as p:  
    # Open a progress log to display the cracking progress.
    
    with open(password_file, "r", encoding='latin-1') as password_list:  
        # Open the password file in read mode, using the Latin-1 encoding for compatibility.
        
        for password in password_list:  
            # Iterate over each line in the password file.
            
            password = password.strip("\n").encode('latin-1')  
            # Remove leading/trailing whitespace and encode the password using Latin-1 encoding.
            
            password_hash = hashlib.sha256sumhex(password)  
            # Compute the sha256 hash of the password and convert it to hexadecimal format.
            
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))   
            # Display the current attempt number, the password being tried, and its hash.
            
            if password_hash == wanted_hash:  
                # Check if the computed hash matches the wanted hash.
                
                p.success(
                    "Pasword hash found after {} attempts! hashes to {}!".format(attempts, password.decode('latin-1')))
                # If a match is found, print a success message with the number of attempts and the cracked password.
                
                exit()  
                # Exit the program since the password has been found.
                
            attempts += 1   
            # Increment the attempt counter for each unsuccessful attempt.
        
        p.failure("Password hash not found")
        # If the loop completes without finding the password, print a failure message.
