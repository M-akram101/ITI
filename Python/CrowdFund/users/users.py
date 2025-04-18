import pickle
import os


class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone

    def show_user_data(self):
        print(f"\nUser Registered Successfully!")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile_phone}")


def load_users(filename="users.pkl"):
    if not os.path.exists(filename):
        return []
    with open(filename, "rb") as file:
        return pickle.load(file)


def save_user(user, filename="users.pkl"):
    users = load_users()
    users.append(user)
    with open(filename, "wb") as file:
        pickle.dump(users, file)
    print("\nUser data saved successfully!")


def register_user():
    print("\nRegister a New User")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    while True:
        email = input("Enter your email: ")
        if "@" in email and "." in email:
            break
        print("Invalid email. Please try again.")

    while True:
        password = input("Enter your password (min 6 chars): ")
        confirm_password = input("Re-enter your password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
        elif password != confirm_password:
            print("Passwords do not match.")
        else:
            break

    while True:
        mobile_phone = input(
            "Enter your mobile phone (11 digits, starts with 010, 011, 012): "
        )
        if (
            mobile_phone.isdigit()
            and len(mobile_phone) == 11
            and mobile_phone.startswith(("010", "011", "012"))
        ):
            break
        print("Invalid phone number. Please try again.")

    user = User(first_name, last_name, email, password, mobile_phone)
    save_user(user)
    user.show_user_data()


def login():
    print("\nLogin")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    users = load_users()

    for user in users:
        if user.email == email and user.password == password:
            print(f"\nWelcome back, {user.first_name}!")
            return user

    print("Invalid email or password.")
    return None
