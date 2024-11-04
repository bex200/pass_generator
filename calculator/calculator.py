def calculator():
    print("Добро пожаловать в калькулятор!\n")
    print("Он умеет считать сразу несколько выражений, например 2.5 + 5 * 3 / 4.7\nДоступные операции:")
    print(" +  : Сложение (например, 2 + 3)")
    print(" -  : Вычитание (например, 5 - 2)")
    print(" *  : Умножение (например, 4 * 3)")
    print(" /  : Деление (например, 9 / 4)\n")
    

    while True:
        # Получаем выражение от пользователя
        expression = input("Введите выражение для вычисления (или 'exit' для выхода): ").strip()

        # Проверяем, хочет ли пользователь выйти
        if expression.lower() == "exit":
            print("Выход из программы.")
            break

        # Проверяем, содержит ли выражение хотя бы один математический оператор
        contains_operator = False
        for op in "+-*/":
            if op in expression:
                contains_operator = True
                break

        # Проверяем деление на ноль вручную
        if "/" in expression:
            parts = expression.split("/")
            if len(parts) > 1 and parts[1].strip() == "0":
                print("Ошибка: деление на ноль невозможно.")
                continue

        # Если выражение содержит оператор, вычисляем его
        if contains_operator:
            result = eval(expression)  # Вычисление выражения
            print(f"Результат: {expression} = {result}")
        else:
            print("Ошибка: Некорректное выражение. Попробуйте снова.")
            
calculator()

# Записать 