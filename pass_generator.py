import random
import datetime
import string


def get_pass_len():
    while True:
        try:
            pass_len = int(input("Введите длину пароля (от 6 до 16): "))
            if 6 <= pass_len <= 16:
                return pass_len
        except ValueError:
            print("ERROR: Введено не числовое значение.", end=" ")


def is_special_symbol():
    is_there_symbol = input("Хотите добавить спец.символы? Да/Нет - ")
    if is_there_symbol.lower() == "да":
        return True
    else:
        return False


def generate_pass(pass_len, is_any_symbol):
    list_of_lower_letters = list(string.ascii_lowercase)
    list_of_upper_letters = list(string.ascii_uppercase)
    list_of_digits = list(string.digits)
    pass_settings = {
        0: list_of_lower_letters,
        1: list_of_upper_letters,
        2: list_of_digits,
    }
    pass_stamp = []

    if is_any_symbol:
        list_of_punctuation = string.punctuation
        pass_settings[3] = list_of_punctuation
    generated_pass = ""

    while True:
        pass_stamp = []
        for each in range(pass_len):
            pass_stamp.append(random.choice(list(pass_settings.keys())))

        if (
            pass_stamp.count(0) == 0
            or pass_stamp.count(1) == 0
            or pass_stamp.count(2) == 0
        ):
            continue
        elif is_any_symbol and max(pass_stamp) != 3:
            continue
        else:
            break

    for i in range(len(pass_stamp)):
        generated_pass += random.choice(pass_settings.get(pass_stamp[i]))

    return generated_pass


def save_pass(final_pass):
    want_to_save = input("Хотите ли сохранить пароль? Да/Нет - ")

    if want_to_save.lower() == "да":
        webservice = input("Для какой платформы пароль? - ")
        date_now = datetime.datetime.now()

        with open("pass.txt", "a", encoding="utf-8") as file:
            result = f"{webservice} ------ {final_pass} -------- {str(date_now.strftime("%d.%m.%Y, %H:%M"))}\n"
            file.write(result)
    else:
        print(final_pass)


def main():
    pass_len = get_pass_len()
    spec_symbol = is_special_symbol()
    final_pass = generate_pass(pass_len, spec_symbol)
    save_pass(final_pass)


main()
