"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2

def main():
    """Program to get and check a user's password."""
    password = get_password()
    for i in range(0, len(password), 1):
        print('*', end='')
    print()

def get_password():
    print("Please enter a valid password")
    print("Your password must be longer than:", MIN_LENGTH)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    return password

def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH:
        return False
    return True

main()