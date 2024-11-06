time = int(input("Введите текущий час (0-23): "))

if time < 12:
    print("Доброе утро!")
elif time < 18:
    print("Добрый день!")
else:
    print("Добрый вечер!")
