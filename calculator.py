import math

deistvie = input("Введите действие, которое хотите выполнить: *, /, +, -, ^ (возведение в степень), % (остаток от деления), sqrt (квадратный корень). Чтобы выйти, введите что-нибудь другое.\n")
while deistvie in ["+", "-", "*", "/", "^", "%", "sqrt"]:
    try:
        if deistvie == "*":
            a = int(input("Введите 1 множитель - "))
            b = int(input("Введите 2 множитель - "))
            print(f"Результат - {a * b}")
        elif deistvie == "/":
            a = int(input("Введите делимое - "))
            b = int(input("Введите делитель - "))
            print(f"Результат - {a / b}")
        elif deistvie == "+":
            a = int(input("Введите 1 слагаемое - "))
            b = int(input("Введите 2 слагаемое - "))
            print(f"Результат - {a + b}")
        elif deistvie == "-":
            a = int(input("Введите уменьшаемое - "))
            b = int(input("Введите вычитаемое - "))
            print(f"Результат - {a - b}")
        elif deistvie == "^":
            a = int(input("Введите основание - "))
            b = int(input("Введите показатель степени - "))
            print(f"Результат - {a ** b}")
        elif deistvie == "%":
            a = int(input("Введите делимое - "))
            b = int(input("Введите делитель - "))
            print(f"Результат - {a % b}")
        elif deistvie == "sqrt":
            a = int(input("Введите число для извлечения квадратного корня - "))
            if a >= 0:
                print(f"Результат - {math.sqrt(a)}")
            else:
                print("Ошибка: корень из отрицательного числа не существует в действительных числах!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: пожалуйста, вводите только целые числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    deistvie = input("Введите действие, которое хотите выполнить еще: *, /, +, -, ^, %, sqrt. Чтобы выйти, введите что-нибудь другое.\n")
else:
    print("Спасибо! До свидания! ^_^")
