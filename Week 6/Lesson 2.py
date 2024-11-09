# Topic - Regular Expressions: Syntax and usage
# Regular expressions (regex) - it is pattern, template for finding text and code for strings
# They help us to find, change, retrieve information in strings based on given template
# By using the regular expressions, we can easily process text with complex structure

#! Main functions are: re.match(), re.search(), re.findall(), re.sub()

#Examples are : emails, city names the prices etc.

import re # Import the module RE, so we can work with regular expressions,

# Example 1: Basic syntax and example of search with regular expressions
def regex_basic_example():
    # Example of template for finding the text "Python" in string
    pattern = r"Python" #Looks for exact "Python", r means that it will be using the regular expressions
    text = "I am learning Python : Python1, Python2, Python3"

    # By using the re.search() for the search of first entries
    match = re.search(pattern, text)
    if match:
        print("There is a match:", match.group())
    else:
        print("There is no match")

# regex_basic_example()

# Example 2: Usage of special symbols
def regex_special_characters():
    text = "Email me at text@example.com or at admin@sample.org."
    # Шаблон для поиска email-адресов
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # \b             - Начало слова, указывает на границу слова
    # [A-Za-z0-9._%+-]+ - Любое сочетание букв, цифр и символов `._%+-`
    # @             - Символ "собачка" в адресах
    # [A-Za-z0-9.-]+ - Домен, включающий буквы, цифры, точки и тире
    # \.            - Обычная точка (экранированная)
    # [A-Z|a-z]{2,} - Окончание домена (2+ букв), например, com, org

    # Используем re.findall() для нахождения всех вхождений
    matches = re.findall(pattern, text)
    print("Найденные email-адреса:", matches)

# regex_special_characters()

#Example 3: Methods of searching: match(), search(), findall, finditer()

def regex_methods_example():
    text = "The price of the item A is $20 and the item B is $35."

    # We use re.match() for searching in the beginning of the line
    match = re.match(r"The price", text)
    if match:
        print("Result of match():", match.group())
    else:
        print("Match is not found")
    # we are gonna use the dollar sign for the first entry
    search = re.search(r"\$\d+", text)
    # \$       - Ищет символ "$" (экранированный)
    # \d+      - Одну или более цифр после "$" (цена)
    if search:
        print("Result of search():", search.group())
    else:
        print("Match is not found")

    # Используем re.findall() для нахождения всех вхождений
    pattern = r"\$\d+"
    all_prices = re.findall(pattern, text)  # Найдет все цены, указанные в тексте
    print("Результат findall():", all_prices)

    # Используем re.finditer() для получения всех совпадений с итерацией
    print("Результат finditer():")
    for match in re.finditer(pattern, text):
        print("Совпадение:", match.group(), "на позиции:", match.start())
    # .start()
    # .group()

# regex_methods_example()

#* === 4. Замена текста с использованием re.sub() ===
def regex_substitute_example():
    text = "The color is red, but it could also be blue or green."

    # Заменяем все цвета на "COLOR"
    pattern = r"red|blue|green"
    # red|blue|green - Ищет слова "red", "blue" или "green" для замены
    replaced_text = re.sub(pattern, "COLOR", text)
    print("Текст после замены:", replaced_text)

# regex_substitute_example()

#* === 5. Using the grouping and backlinking ===
def regex_grouping_example():
    text = "My phone number is (123) 456-7890."

    # Group the parts of the telephone number:
    pattern = r"\((\d{3})\) (\d{3})-(\d{4})"
    # \(          - Открывающая скобка "(" (экранированная)
    # (\d{3})     - Группа: три цифры для кода города
    # \)          - Закрывающая скобка ")" (экранированная)
    # (\d{3})     - Группа: три цифры (первые три цифры номера)
    # -           - Символ "-"
    # (\d{4})     - Группа: четыре цифры (последняя часть номера)

    # Используем re.search() для поиска с группировкой
    match = re.search(pattern, text)
    if match:
        print("Полный номер:", match.group(0))  # Полный номер
        print("Код города:", match.group(1))  # Код города
        print("Первые три цифры:", match.group(2))  # Первые три цифры
        print("Последние четыре цифры:", match.group(3))  # Последние четыре цифры

regex_grouping_example()

#* === 6. Example of validation and format checking ===
def regex_validation_example():
    #Checking the correctness of format of email
    email = input("Please enter your email: ")
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$"
    # ^              - Начало строки - string it should start with everything that will be stated right after ^
    # [A-Za-z0-9._%+-]+ - Сочетание символов для локальной части email
    # @              - Символ "@"
    # [A-Za-z0-9.-]+ - Доменное имя
    # \.             - Точка перед доменом верхнего уровня
    # [A-Z|a-z]{2,}  - Минимум две буквы для домена верхнего уровня
    # $              - Конец строки
    if re.match(pattern, email):
        print("Email в корректном формате.")
    else:
        print("Неверный формат email!")

# regex_validation_example()
#Homework 1
def regex_validation_example():
    #Checking the correctness of format of email
    email = input("Please enter your email: ")
    pattern = r"^[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}|[A-Za-z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
    # ^              - Начало строки - string it should start with everything that will be stated right after ^
    # [A-Za-z0-9._%+-]+ - Сочетание символов для локальной части email
    # @              - Символ "@"
    # [A-Za-z0-9.-]+ - Доменное имя
    # \.             - Точка перед доменом верхнего уровня
    # [A-Z|a-z]{2,}  - Минимум две буквы для домена верхнего уровня
    # $              - Конец строки
    if re.match(pattern, email):
        print("Email в корректном формате.")
    else:
        print("Неверный формат email!")

# regex_validation_example()

#Homework 2
def regex_validation_example():
    #Checking the correctness of format of email
    email = input("Please enter your email: ")
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(edu\.)?[Kk][Zz]$"
    # ^              - Начало строки - string it should start with everything that will be stated right after ^
    # [A-Za-z0-9._%+-]+ - Сочетание символов для локальной части email
    # @              - Символ "@"
    # [A-Za-z0-9.-]+ - Доменное имя
    # \.             - Точка перед доменом верхнего уровня
    # [A-Z|a-z]{2,}  - Минимум две буквы для домена верхнего уровня
    # $              - Конец строки
    if re.match(pattern, email):
        print("Email в корректном формате.")
    else:
        print("Неверный формат email!")

# regex_validation_example()

