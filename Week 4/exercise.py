# Creation of file and writing a numbers

def create_and_write_numbers_intonewfile():
    """Creating a file and writing numbers into it"""
    with open("numbers.txt", "w") as file:
        numbers = [10, 20, 30, 40, 50]
        for number in numbers:
            file.write(f"{number}\n")

create_and_write_numbers_intonewfile()

#Writing numbers from file and doing some calculations

def read_numbers_and_calculate():
    """Reads and calculates"""
    numbers = []

    with open("numbers.txt", "r") as file:
        for line in file: # Reads file line by line when we use the loops just with itself
            number = int(line.strip()) #converting string to integer, strip is a method that we need to convert
            numbers.append(number)
    total = sum(numbers)
    average = total / len(numbers)
    maxima = max(numbers) #Maximum

    print(f"Sum: {total}")
    print(f"Mean: {average}")
    print(f"Maximum value: {maxima}")

read_numbers_and_calculate()