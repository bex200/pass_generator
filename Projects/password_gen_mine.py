# random - рандомайзер от питона
# datetime - to track the time of password creation
# string - library, which as all the latin letters and numbers and symbols capital lowercase everything

# For each stage of the code we create separate functions

import random
import datetime
import string

# Stage 1: Function for length of the password

def password_length():
    while True:
        try:
            password_len = int(input("Enter a length of the password from 6 to 16: "))
            if (password_len >= 6) and (password_len <= 16):
                return password_len
            else:
                print("Enter a number between 6 and 16")
        except ValueError:
            print("Error: enter please a number not a symbol or letter!")
         #return stops everything even the infinite loop

# password_length()

# Step 2: Is there any special chracter you want in your passsword

def is_special_character():
    is_there_symbol = input("Do you want to add special symbols to the password? Yes/No ")
    if is_there_symbol.lower() == "yes":
        return True
    else:
        return False

# true_or_false = is_special_character()
# print(true_or_false)

def generate_password(password_len, is_special_character):
    string_of_all_elements = string.ascii_letters + string.digits
    string_of_letters = string.ascii_letters
    string_of_digits = string.digits
    generated_password = ""
    if is_special_character:
        string_of_punctuation = string.punctuation
        string_of_all_elements += string.punctuation
        for element in range(password_len-3):
            generated_password += random.choice(string_of_all_elements)
        generated_password += random.choice(string_of_letters) + random.choice(string_of_digits) + random.choice(string_of_punctuation)
        return generated_password
    else:
        # Generate password without special characters
        for element in range(password_len-2):
            generated_password += random.choice(string_of_all_elements)
        generated_password += random.choice(string_of_letters) + random.choice(string_of_digits)
        return generated_password
def save_password(generated_password):
    want_to_save = input("Do you want to save your password? Yes/No \n ")
    if want_to_save.lower() == "yes":
        website = input("For which platform the password was created? \n ")
        date_string = datetime.datetime.now()
        date_now = date_string.strftime('%m/%d/%y %H:%M:%S')

        with open("passwords.txt", "a", encoding = "utf-8") as file:
            result = f" {website}   - {generated_password}  -  {str(date_now)} \n"
            file.write(result)
    else:
        print("Okay, not saved!")
        return

    print("Successfully saved!")
    return

def main():
    password_len = password_length()
    any_symbol = is_special_character()
    final_password = generate_password(password_len, any_symbol)
    save_password(final_password)
    print(final_password)
    return final_password

main()