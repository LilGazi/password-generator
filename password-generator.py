import random
import string

rerun = True

while rerun:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your generated password is:", password)

    choice = input("Do you want to continue? ").lower()

    if choice != "yes":
        rerun = False
        print("Goodbye!")
