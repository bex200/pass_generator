import re
def regex_special_characters():
    text = "Email me at test123@example.com or at admin@sample.org, test123@example.com, test123@example.com"
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    matches = re.findall(pattern, text)
    print("Найденные email-адреса:", matches)

# Вызов функции
regex_special_characters()