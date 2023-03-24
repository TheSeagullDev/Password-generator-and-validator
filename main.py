import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMS = "0123456789"
SYMBOLS = "!@#$%^&*()?+-_="
GENERATE_PASSWORD = "1"
VALIDATE_PASSWORD = "2"

def get_password(charset, length):
    password = ""
    for char in range(length):
        password += charset[random.randrange(len(charset))]
    return password

def generate_charset(letters, numbers, symbols):
    while True:
        selection = input("Enter: ")
        if selection.isdigit():
            selection = int(selection)
            if selection == 1:
                chars = letters
                break
            elif selection == 2:
                chars = letters + numbers
                break
            elif selection == 3:
                chars = letters + symbols
                break
            elif selection == 4:
                chars = letters + numbers + symbols
                break
            else:
                print("Please enter a number from 1 to 4")
        else:
            print("Please enter a valid number")
    return chars

def generate_password():
    print("Please select character types: \n1: Uppercase and lowercase letters\n2: Letters and numbers\n3: Letters and symbols\n4: Letters and numbers and symbols")

    charset = generate_charset(LETTERS, NUMS, SYMBOLS)
    while True:
        length = input("Enter password length: ")
        if length.isdigit():
            length = int(length)
            break
        else:
            print("Please enter a number")

    print(f"Your password is: {get_password(charset, length)}")

def validate_password():
    print("Feature not yet implemented")

print("Please select: \n1: Generate password \n2: Validate Password")
while True:
    choice = input()
    if choice == GENERATE_PASSWORD:
        generate_password()
        break
    elif choice == VALIDATE_PASSWORD:
        validate_password()
        break
    else:
        print("Invalid choice")