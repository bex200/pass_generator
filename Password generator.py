import random
import datetime
import string

#Постановка задачи: сформировать пароль, который из состоит хотя бы из 1 буквы, 1 цифры и 1 символа 

#В этой функции ничего не меняла из вашего кода
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

#Конец подогнала, сохранить необходимо будет финальный обрезанный пароль :) 
def generate_password(pass_len):
    password = ''

    for element in range(pass_len):
        password += random.choice(string.ascii_letters)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        
    print(password[0:pass_len])

    return password[0:pass_len]


#В этой функции ничего не меняла из вашего кода
def save_password(password):
    want_to_save = input('Хотите ли сохранить пароль? Да/Нет\n')

    if want_to_save.lower() == 'да':
        website = input('Для какой платформы создали данный пароль?\n')
        date_now = datetime.datetime.now()

        with open('passwords.txt', 'r+', encoding='utf-8') as file:
            result = f'{website} ------ {password} ----- {str(date_now)}'
            file.write(result)
    else:
        print('Мы удивлены вашей уверенностью в своей памяти. Хорошего дня!')
        return

    print('Ваш пароль вы можете найти в текстовом файле passwords.txt')
    return



def main():
    password_len = get_password_len()
    final_password = generate_password(password_len)
    save_password(final_password)

main()