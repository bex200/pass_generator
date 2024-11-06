deistvie = input("Введите действие которое хотите выполнить еще: *,/,+,-")
while deistvie == "+" or deistvie == "-" or deistvie == "/" or deistvie == "*":
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
    deistvie = input("Введите действие которое хотите выполнить еще: *,/,+,-. Если хотите закончить напишите что ни будь")
else:
    print("Спасибо! До свидания! ^_^")
