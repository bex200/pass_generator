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
        level_of_password = int(input("""Введите уровень сложности пароля:
                         1 - Легкий
                         2 - Средний
                         3 - Сложный\n"""))
        if level_of_password in(1,2,3):
            print("Принято!")
            return(level_of_password)
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
def get_password(level_password, password_len):
    nltk.download("words")  # Грузим слова из библиотеки
    word_list = []
    digit_list = string.digits
    symbol_list = string.punctuation
    word_symbol_digit_list = string.ascii_letters + string.digits + string.punctuation
    
    # Блок для 1 уровня сложности пароля
    if level_password == 1:
        for word in words.words():
            if len(word) == password_len:
                word_list.append(word)
        return random.choice(word_list)

    # Блок для 2 уровня сложности пароля
    elif level_password == 2:
        # Создаю рандомное количество цифр в конце слова... -1 делаю что бы пароль не состоял из одних цифр
        random_amount_of_digits = random.randint(1, password_len-1)         
        for word in words.words():
            # проверяю длину найденного слова что бы не превышало запрашиваемое(в общем объеме)
            if len(word) == password_len - random_amount_of_digits:
                word_list.append(word)
        return random.choice(word_list) + ''.join(random.choices(digit_list, k=random_amount_of_digits))
    
    # Блок для 3 уровня сложности пароля
    elif level_password == 3:
        # Создаю рандомное количество цифр в конце слова... -1 делаю что бы пароль не состоял из одних цифр
        random_amount_of_digits = random.randint(1, password_len-1)
        # Создаю рандомное количество символов в конце слова... -1 делаю что бы пароль не состоял из одних цифр или символов
        random_amount_of_symbols = random.randint(1,password_len - random_amount_of_digits - 1)
        for word in words.words():
            # проверяю длину найденного слова что бы не превышало запрашиваемое(в общем объеме)
            if len(word) == password_len- random_amount_of_digits - random_amount_of_symbols:
                word_list.append(word)
        return random.choice(word_list) + ''.join(random.choices(digit_list, k=random_amount_of_digits)) + ''.join(random.choices(symbol_list, k=random_amount_of_symbols))
    
    # Блок для пароля из набора букв и символов
    elif level_password not in [1,2,3]:
        password = ""
        for word in range(password_len):
            password += random.choice(word_symbol_digit_list)
        return password
    
 
def save_password(password_ready): 
    website = input("Введите пароль для какой платформы:\n")
    with open("passwords.txt", "a", encoding="utf-8") as file:
        # сохраняет пароль в файл
        file.write(f"{website} ---- {password_ready} ---- {datetime.now().strftime('%b-%d-%Y %H:%M')}\n")      
        # выводит сайт-пароль-время в терминал                                  
        return (f"Ваша запись сохранена:\n{website} ---- {password_ready} ---- {datetime.now().strftime('%b-%d-%Y %H:%M')}\n")          
    
def main():
    password = get_password_len()                       # Функция для ввода длины пароля
    level = get_level_of_password()                     # Функция для выбора уровня пароля
    password_final = get_password(level, password)      # Функция для генерации пароля
    print(save_password(password_final))                # Функция для сохранения пароля в блакнот
    
main()
