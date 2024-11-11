
#! random - рандомайзер от пайтона
#! datetime - узнавать время и дату
#! string - символы

import random
import datetime
import string

# Функция для длины пароля
def get_password_len():
    while True:
        try:
            password_len = int(input("Введите длину пароля (от 6 до 16):"))
            if (password_len >= 6) and (password_len <= 16):
                return password_len
            else:
                print('Введите числа в интервале (от 6 до 16)') 
        except ValueError:
            print('ERROR: Введите числовое значение')

            
def is_special_symbol():
    is_there_symbol = input('Хотите добавить спец. символы? Да/Нет\n')
    if is_there_symbol.lower() == 'да':
        return True
    else:
        return False


def generate_password(pass_len, is_special_symbol):
    string_of_all_elements = string.ascii_letters + string.digits
    
    if is_special_symbol:
        string_of_all_elements += string.punctuation
    
    password = ''

    for element in range(pass_len):
        password += random.choice(string_of_all_elements)
    
    print(password)

    return password

def save_password(password):
    want_to_save = input('Хотите ли сохранить пароль? Да/Нет\n')

    if want_to_save.lower() == 'да':
        website = input('Для какой платформы создали данный пароль?\n')
        date_now = datetime.datetime.now()

        with open('passwords.txt', 'r+', encoding='utf-8') as file:
            result = f'{website} ------ {password} ----- {str(date_now)}'
            file.write(result)
    else:
        print('Хорошо, УДАЧИИ))), Удачи вспоминать когда понадобиться')
        return

    print('Успешно всё сохранили!!!!!!')
    return

def main():
    password_len = get_password_len()
    any_symbols = is_special_symbol()    
    final_password = generate_password(password_len, any_symbols)
    save_password(final_password)

main()








    
