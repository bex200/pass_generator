import random

# Генерируем случайное число от 1 до 10
number_to_guess = random.randint(1, 10)

while True:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess == number_to_guess:
        print("Поздравляем, вы угадали!")
        break
    elif guess < number_to_guess:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
