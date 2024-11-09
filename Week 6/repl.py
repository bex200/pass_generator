
# ? === Тема: Регулярные выражения: Синтаксис и использование ===
# * Регулярные выражения (regex) — это шаблоны для поиска текста и работы со строками.
# Они позволяют находить, изменять или извлекать информацию в строках на основе заданных шаблонов.
# Используя регулярные выражения, мы можем легко обрабатывать текст с сложными структурами.
# ! Основные функции: re.match(), re.search(), re.findall(), re.sub()

import repl  # Импортируем модуль re для работы с регулярными выражениями


# * === 1. Базовый синтаксис и пример поиска с помощью регулярных выражений ===
def regex_basic_example():
    # Пример шаблона для поиска текста "Python" в строке
    pattern = r"Python"  # Ищет точное совпадение с текстом "Python"
    text = "I am learning Python programming. Python12, Pythonq, Python, Python09"

    # ! Используем re.search() для поиска первого вхождения
    match = re.search(pattern, text)
    if match:
        print("Найдено совпадение:", match.group())
    else:
        print("Совпадение не найдено.")

# regex_basic_example()

# * === 2. Использование специальных символов ===
def regex_special_characters():
    text = "Email me at test123@example.com or at admin@sample.org, test123@example.com, test123@example.com "

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

# * === 3. Методы поиска: match(), search(), findall(), finditer() ===
def regex_methods_example():
    text = "The price of item A is $20 and item B is $35."

    # Используем re.match() для поиска в начале строки
    match = re.match(r"The price", text)  # Ищет "The price" только в начале строки
    if match:
        print("Результат match():", match.group())
    else:
        print("Совпадение не найдено.")

    # Используем re.search() для поиска первого вхождения
    search = re.search(r"\$\d+", text)
    # \$       - Ищет символ "$" (экранированный)
    # \d+      - Одну или более цифр после "$" (цена)
    print("Результат search():", search.group() if search else "Совпадение не найдено.")

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

regex_methods_example()



