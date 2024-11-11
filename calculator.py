def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"
    elif operation == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Ошибка: деление на ноль"
    elif operation == "**":
        return num1 ** num2
    elif operation == "//":
        if num2 != 0:
            return num1 // num2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция!"

name = input('Как твое имя, странник: ')
print(f"{name}, добро пожаловать в мой маленький примитивный калькулятор!")
while True:
    try:
        num1 = int(input("Введи первое число: "))
        act = input("Введи желаемое действие (+, -, *, /, %, **, //): ")
        num2 = int(input("Введи второе число: "))
        result = calculator(num1, num2, act)
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введено некорректное число.")
    
    answer = input('Хотите сделать еще одну операцию? Да/Нет: ')
    if answer.lower() == 'нет':
        break
