import hashlib
import getpass

password_manager = {}


def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
    print(hashed_pwd)
    password_manager[username] = hashed_pwd
    print("account created successfully!")


def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

    if username in password_manager.keys() and password_manager[username] == hashed_pwd:
        print("Login successfully!")
    else:
        print("Invalid username or password.")


def main():
    while True:
        choice = int(input("Enter 1 to create an account, 2 to login or 0 to exit: "))
        match choice:
            case 1:
                create_account()
            case 2:
                login()
            case 0:
                break
            case _:
                print("Invalid choice.")


if __name__ == '__main__':
    main()
