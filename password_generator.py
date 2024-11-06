import random
from datetime import datetime
import string
import nltk
from nltk.corpus import words


# Узнаем длину генерируемого пароля
def get_password_len():
    while True:
        try:
            password_len = int(input("Введите длину пароля от 6 до 12:\n"))
            if 12>=password_len>= 6:
                print("Принято!")
                return password_len
            elif password_len<6:
                print("ERROR: Введите число больше 6")
            else:
                print("ERROR: Введите число меньше 12")
        except ValueError:
            print("ERROR: Введите целое число от 6 до 12 включительно:\n")

    

# Узнаем какой уровень сложности хочет пользователь для своего пароля
def get_level_of_password():
    try:
        (lvl_of_pass) = int(input("""Введите уровень сложности пароля:
                         1 - Легкий
                         2 - Средний
                         3 - Сложный\n"""))
        if (lvl_of_pass) in(1,2,3):
            print("Принято!")
            return((lvl_of_pass))
        else: 
            print("""Не ввел верно ;) Получил пароль сложный, удачи запомнить""")
            return 4
    # Исключение если пользователь не вводит ничего
    except ValueError:
        print("""Введите уровень сложности пароля:
                         1 - Легкий
                         2 - Средний
                         3 - Сложный""")
        return get_level_of_password()


# Генератор пароля
def get_password(lvl_pass, pass_len):
    nltk.download("words")  # Грузим слова из библиотеки
    word_list = []
    digit_list = string.digits
    symbol_list = string.punctuation
    word_symbol_digit_list = string.ascii_letters + string.digits + string.punctuation
    
    # Блок для 1 уровня сложности пароля
    if lvl_pass == 1:
        for word in words.words():
            if len(word) == pass_len:
                word_list.append(word)
        return random.choice(word_list)

    # Блок для 2 уровня сложности пароля
    elif lvl_pass == 2:
        # Создаю рандомное количество цифр в конце слова... -1 делаю что бы пароль не состоял из одних цифр
        rnd_digits = random.randint(1, pass_len-1)         
        for word in words.words():
            # проверяю длину найденного слова что бы не превышало запрашиваемое(в общем объеме)
            if len(word) == pass_len - rnd_digits:
                word_list.append(word)
        return random.choice(word_list) + ''.join(random.choices(digit_list, k=rnd_digits))
    
    # Блок для 3 уровня сложности пароля
    elif lvl_pass == 3:
        # Создаю рандомное количество цифр в конце слова... -1 делаю что бы пароль не состоял из одних цифр
        rnd_digits = random.randint(1, pass_len-1)
        # Создаю рандомное количество символов в конце слова... -1 делаю что бы пароль не состоял из одних цифр или символов
        rnd_symbol = random.randint(1,pass_len - rnd_digits - 1)
        for word in words.words():
            # проверяю длину найденного слова что бы не превышало запрашиваемое(в общем объеме)
            if len(word) == pass_len- rnd_digits - rnd_symbol:
                word_list.append(word)
        return random.choice(word_list) + ''.join(random.choices(digit_list, k=rnd_digits)) + ''.join(random.choices(symbol_list, k=rnd_symbol))
    
    # Блок для пароля из набора букв и символов
    elif lvl_pass not in [1,2,3]:
        password = ""
        for word in range(pass_len):
            password += random.choice(word_symbol_digit_list)
        return password
    
 
def save_password(pass_ready): 
    website = input("Введите пароль для какой платформы:\n")
    with open("passwords.txt", "a", encoding="utf-8") as file:
        # сохраняет пароль в файл
        file.write(f"{website} ---- {pass_ready} ---- {datetime.now().strftime('%b-%d-%Y %H:%M')}\n")      
        # выводит сайт-пароль-время в терминал                                  
        return (f"Ваша запись сохранена:\n{website} ---- {pass_ready} ---- {datetime.now().strftime('%b-%d-%Y %H:%M')}\n")          
    
def main():
    password = get_password_len()                       # Функция для ввода длины пароля
    level = get_level_of_password()                     # Функция для выбора уровня пароля
    password_final = get_password(level, password)      # Функция для генерации пароля
    print(save_password(password_final))                # Функция для сохранения пароля в блакнот
    
main()
