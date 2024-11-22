import secrets  # It's just so much better than random
import string
import datetime


# GitHub: @Milterdone
# Vladislav Goncharov
def get_password_length():
    length = None
    try:
        length = int(input("How long would you like your password? (6-20): "))
    except ValueError:
        print("Please enter a number.")
        return get_password_length()
    finally:
        if length and (length < 6 or length > 20):
            print("Please enter a number between 6 and 20.")
            return get_password_length()
        else:
            return length


def include_special_characters():
    check = input("Do you want to include special characters? (y/n): ").lower().strip()
    if check in ("y", "yes"):
        return True
    elif check in ("n", "no"):
        return False
    else:
        print("Please enter y or n.")
        return include_special_characters()


def generate_password(length, use_special_chars):
    password = ''
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation
    for i in range(length):
        password += secrets.choice(chars)
    return password


def save_password(password):
    for_what = input("For which app or site do you need this password?:\n")
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"Your password is: {password}\n"
                       f"It's for: {for_what}\n"
                       f"At date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n")
        print("Password saved successfully.")
    except FileNotFoundError:
        print("Error: The file 'passwords.txt' does not exist.")
        print("Creating the password.txt file...")
        with open("password.txt", "w"):
            file.write("===== PASSWORDS FILE ======")
        save_password(password)
    except PermissionError:
        print("Error: Permission denied. Cannot write to 'passwords.txt'.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


def main():
    length = get_password_length()
    including_sc = include_special_characters()
    password = generate_password(length, including_sc)
    save_password(password)


main()
