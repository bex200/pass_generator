import random
import datetime
import string

# function for the password's length
def get_password_len():
    while True:
        try:
            password_len = int(input("Enter the len of password (from 0 to 16):"))
            if (password_len >= 6) and (password_len <= 16):
                return password_len
            else:
                print("Enter data in between 6 and 16")
        except ValueError:
            print("Enter numeric data")



def is_special_symbol():
        is_there_symbol = input("Want to add symbols? Yes/No\n")
        if is_there_symbol.lower() == "yes":
            return True
        else:
            return False
        
# true_or_false = is_special_symbol()
# print(true_or_false)

def generate_password(pass_len, is_special_symbol):
    string_of_all_elements = string.ascii_letters + string.digits

    if is_special_symbol:
        string_of_all_elements += string.punctuation

    password = ""

    for element in range(pass_len):
        password += random.choice(string_of_all_elements)
    print(password)
    return password


# password = generate_password(7, True)
# print(password)

def save_password(password):
    want_to_save = input("Do you want to keep the password? Yes/No\n")
    
    if want_to_save.lower() == "yes":
        website = input("For which website this password was generated?\n")
        date_now = datetime.datetime.now()
        #first datetime is for library, second one is for class

        with open("passwords.txt", "r+", encoding='utf-8') as file: #here we use r+ bc "w" erases everything
            result = f"{website} ------ {password} ------ {str(date_now)}"
            file.write(result)
    else:
        print("Okay, good luck remembering it when needed")
        return #after this nothing will be read 
    

    print("Successfully saved")
    return #in this case return is not necassary

def main():
    password_len = get_password_len() #After user will go through all of the needed steps, data will ve saved here
    any_symbols = is_special_symbol() #you can name a variable with the same name as function, but that will not look good
    final_password = generate_password(password_len, any_symbols)
    save_password(final_password)

main()