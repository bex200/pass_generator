import re
def regex_basic_example():
    pattern = r"Python"  # Шаблон для поиска точного совпадения "Python"
    text = "I am learning Python programming. Python12, Pythonq, Python, Python09"

    match = re.search(pattern, text)
    if match:
        print("Найдено совпадение:", match.group())
    else:
        print("Совпадение не найдено.")

# Вызов функции
regex_basic_example()
