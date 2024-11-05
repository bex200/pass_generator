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
    list_of_elements = list(string.ascii_letters) + list(string.digits)
    if is_any_symbol:
        list_of_elements.extend(string.punctuation)
    generated_pass = ""
    for element in range(pass_len):
        generated_pass += random.choice(list(list_of_elements))
    return generated_pass


def save_pass(final_pass):
    want_to_save = input("Хотите ли сохранить пароль? Да/Нет - ")

    if want_to_save.lower() == "да":
        webservice = input("Для какой платформы пароль? - ")
        date_now = datetime.datetime.now()

        with open("pass.txt", "a", encoding="utf-8") as file:
            result = f"{webservice} ------ {final_pass} -------- {str(date_now)}\n"
            file.write(result)
    return


def main():
    pass_len = get_pass_len()
    spec_symbol = is_special_symbol()
    final_pass = generate_pass(pass_len, spec_symbol)
    save_pass(final_pass)


main()
