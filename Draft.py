animal_name = input("Введите название животного: ")

animal_type = input("Введите тип животного (wild or not wild):  ")

if animal_type == "wild":
    print(f"{animal_name} is a wild animal and eats meat")
else:
    print(f"{animal_name} is not a wild animal and does not eat meat")