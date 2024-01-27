
import getpass


def add_user(username, real_name, password): 
    if check_existing_username(username):
        print("Error: Username already exists. Please choose a different username.")
    else:
        with open('passwd.txt', 'a') as f:
            f.write(f"{username}:{real_name}:{password}\n")
        print("User Created.")

def check_existing_username(username):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()
        existing_usernames = [line.split(':')[0] for line in lines]
        return username in existing_usernames



def change_password(username, current_password, new_password):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines() 

    found = False
    with open('passwd.txt', 'w') as f:
        for line in lines:
            if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                found = True
                f.write(f"{username}:{line.split(':')[1]}:{new_password}\n")
            else:
                f.write(line)

    if found:
        print("Password changed.")
    else:
        print("User not found or current password is incorrect. Nothing changed.")


def delete_user(username):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()

    found = False
    with open('passwd.txt', 'w') as f:
        for line in lines:
            if not line.startswith(f"{username}:"):
                f.write(line)
            else:
                found = True

    if found:
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")



def login(username, password):
    with open('passwd.txt', 'r') as f:
        for line in f:
            u, _ , p = line.strip().split(':')
            if u == username and p == password:
                print("Access granted.")
                return

    print("Access denied.")


if __name__ == "__main__":
    
    choice = input("Choose operation \n (1: Change Password \n 2: Delete User\n 3: Login\n 4: Add User)\n  Enter number for choosing the operation: ")

    if choice == '1':
        username = input("User: ")
        current_password = input("Current Password: ")
        new_password = input("New Password: ")
        confirm_password = input("Confirm: ")

        if new_password == confirm_password:
            change_password(username, current_password, new_password)
        else:
            print("Passwords do not match. Nothing changed.")

    elif choice == '2':
        username = input("Enter username: ")
        delete_user(username)

    elif choice == '3':
        username = input("User: ")
        password = input("Password: ")
        login(username, password)

    elif choice == '4':
        username = input("Enter new username: ")
        real_name = input("Enter real name: ")
        password = getpass.getpass("Enter password: ")  # Use getpass for secure password input
        add_user(username, real_name, password)

    else:
        print("Invalid choice.")
