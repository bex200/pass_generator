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

    if is_special_character:
        string_of_all_elements += string.punctuation
    generated_password = ""
    for element in range(password_len):
        generated_password += random.choice(string_of_all_elements)

    print(generated_password)

    return generated_password

password = generate_password(7, True)
print(password)

def save_password(generated_password):
    want_to_save = input("Do you want to save your password? Yes/No \n ")


    if want_to_save.lower() == "yes":
        website = input("For which platform the password was created? \n ")
        date_now = datetime.datetime.now()

        with open("passwords.txt", "r+", encoding = "utf-8") as file:
            result = f" {website}   - {generated_password}  -  {str(date_now)} "
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
    return final_password


main()

    #
    #
    # if (is_any_symbol == True):
    #     list_of_all_elements.append(string.punctuation)
    #
    # generated_password = ''
    #
    # for element in range(pass_len):
    #     generated_password += random.choice(list_of_all_elements)
