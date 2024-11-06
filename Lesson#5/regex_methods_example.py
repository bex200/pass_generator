import re
def regex_methods_example():
    text = "The price of item A is $20 and item B is $35."
    
    match = re.match(r"The price", text)
    if match:
        print("Результат match():", match.group())
    
    search = re.search(r"\$\d+", text)
    print("Результат search():", search.group() if search else "Совпадение не найдено.")
    
    pattern = r"\$\d+"
    all_prices = re.findall(pattern, text)
    print("Результат findall():", all_prices)
    
    print("Результат finditer():")
    for match in re.finditer(pattern, text):
        print("Совпадение:", match.group(), "на позиции:", match.start())

# Вызов функции 
regex_methods_example()