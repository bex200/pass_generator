import random
import string
from datetime import datetime
import os

def generate_password():
    # Получаем длину пароля
    while True:
        try:
            length = int(input("Введите длину пароля от 6 до 16 символов: "))
            if 6 <= length <= 16:
                break
            else:
                print("Пожалуйста, введите число от 6 до 16.")
        except ValueError:
            print("Нужно ввести целое число.")

    # Спрашиваем про использование спецсимволов
    use_special_chars = input("Использовать спецсимволы? (да/нет): ").strip().lower()
    include_special = use_special_chars == 'да'

    # Формируем набор символов
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Сгенерированный пароль: {password}")

    # Предлагаем сохранить пароль в файл
    save_password = input("Сохранить пароль в файл? (да/нет): ").strip().lower()
    if save_password == 'да':
        # Запрашиваем ресурс
        resource = input("Введите название ресурса для которого сгенерировали пароль: ").strip()
        
        # Запрашиваем путь для сохранения файла или используем путь по умолчанию
        user_path = input("Введите путь для сохранения файла (нажмите Enter для сохранения по умолчанию на диск C): ").strip()
        if not user_path:
            user_path = "C:\\"
        
        # Убедимся, что директория существует
        if not os.path.exists(user_path):
            os.makedirs(user_path)

        # Запрашиваем название файла
        file_name = input("Введите название файла (без расширения): ").strip() + ".txt"
        
        # Полный путь к файлу
        file_path = os.path.join(user_path, file_name)

        # Формируем строку для записи
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_string = f"{resource} - {password} - {current_time}\n"

        # Открываем файл в режиме добавления и записываем строку
        with open(file_path, "a") as file:
            file.write(save_string)
        
        print("Пароль успешно сохранен.")
    else:
        print("Зря конечно, ну ок.")

# Запуск генератора пароля
generate_password()