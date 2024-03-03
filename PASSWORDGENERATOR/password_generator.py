import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("How many character of number password you need? Enter a number: "))
        if length <= 0:
            print("Invalid input. Please enter a positive number for the password length.")
            return f"Generate password agian!"

        password = generate_password(length)
        print(f"Your generated password is: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    password_generator()
