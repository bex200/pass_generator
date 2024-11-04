def create_and_write_numbers():
    with open("numbers.txt", "w") as file:
        numbers = [10,30,45,65,98,232]
        for number in numbers:
            file.write(f"{number}\n")

create_and_write_numbers()