import random
import datetime
import string 

def greet():
    print(f"Hello! Welcome to the password generator.")

def get_password_len():
    while True:
        try: 
            password_len = int(input("Choose length: 5-15:"))
            if password_len < 5:
                print("ERROR: Length must be at least 5.")
            elif password_len > 15:
                print("ERROR: Length must be no more than 15.")
            else:
                return password_len
        except ValueError:
            print("ERROR! Please enter a number between 5 and 15.")

def is_special_symbol():
    while True:
        special_symbols = input("Do you want special symbols? Yes/No:")
        if special_symbols.lower() == "yes":
            return True
        elif special_symbols.lower() == "no":
                return False  
        else:
            print("Please, choose 'Yes' or 'No'.")   

def generate_password(length, use_special_symbols):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if use_special_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
    
def save_password(password):
    while True:
        want_to_save = input("Do you want to save password? Yes/No:")
        if want_to_save.lower() == "yes":
            website = input("For which platform?\n")
            date_now = datetime.datetime.now().strftime("%d-%B-%Y - %I:%M:%p")
            result = f"{website}-----{password}-----{str(date_now)}\n"
            with open("password.txt", "a") as file:
                file.write(result)
            print("Password saved successfully.")
            return True
        elif want_to_save.lower() == "no":
            print("Ok. Good luck!")
            return False
        else:
            print("Please, choose 'Yes' or 'No'.")

def another_password():
    while True:
        repeat = input("Do you want to generate another password? Yes/No: ")
        if repeat.lower() == "yes": 
            return True
        elif repeat.lower() == "no":
            print("Goodbye!")
            return False
        else:
            print("Please, choose 'Yes' or 'No'.")
        
def change_password(password, length, use_special_symbols):
    while True:
        like_password = input(f"Do you like this password? '{password}' Yes or No: ")
        if like_password.lower() == "yes":
            return password
        elif like_password.lower() == "no":
            print("Generating new password...")
            password = generate_password(length, use_special_symbols)  
        else:
            print("Please choose 'Yes' or 'No'.")


def main():
    greet()
    while True:
        password_length = get_password_len()
        use_special = is_special_symbol()
        password = generate_password(password_length, use_special)
        password = change_password(password, password_length, use_special)
        print("Generated password:", password)
        save_password(password)
        if not another_password():
            break   
main()

#Доп функции которые можно добавить: проверка на силу пароля, способность менять пароль который уже был сохранён,
#Вывод всех паролей в терминале если пользователь захочет, способность отправки паролей на почту пользователя,
#