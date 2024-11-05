#! random - рандомайзер
#! datetime - дата
#! string - символы

import random as rd
import datetime as dt
import string as stri
import secrets

# Функция для длины пароля

def get_password_len():
    while True:
        try:
             password_len = int(input('Введите длину пароля от 6 до 16 знаков: '))
             if (password_len >= 6) and (password_len <= 16):
                return password_len    
             else:
                print('Неверная длина пароля! Будьте повнимательнее!')
        except ValueError:
             print('Введите числовое значение!')

def is_special_symbol():
    while True:
        is_there_symbol = input('Хотите добавить специальные символы? Да/Нет: ')        
        if is_there_symbol.lower() == 'да':
            return True
        elif is_there_symbol.lower() == 'нет':
            return False
        else:
            print('Можно ответить только ДА или НЕТ!')
        

def generate_password(password_len, is_special_symbol):
    str_of_all_elements = stri.ascii_letters + stri.digits
    if is_special_symbol == True:
        str_of_all_elements += stri.punctuation

    password = ''  

    for element in range(password_len):    
        password += secrets.choice(str_of_all_elements)

    print(password)

    return password

def save_password(password):
    want_to_save = input('Хотите ли сохранить пароль? Да/Нет\n')

    if want_to_save.lower() == 'да':
        website = input('Для какой платформы создан данный пароль?\n')
        date_now = dt.datetime.now()
        form_time = date_now.strftime('%d.%m.%Y %H:%M')
        while True: 
            try:
                with open('passwords.txt', 'a', encoding='utf-8') as file:
                    result = (f'{website} ---- {password} ---- {form_time}')
                    file.write(result)
                    print('Сохранение выполнено!')
                    return
            except PermissionError:
                print('У вас недостаточно прав, для октрытия этого файла')
    else:
        print('Ок, приходили люди в черном, я уже забыл пароль, впрочем, как и ты послезавтра')
        return    

def main():
    password_len = get_password_len()
    any_symbols = is_special_symbol()
    final_password = generate_password(password_len, any_symbols)
    save_password(final_password)

main()
    
    