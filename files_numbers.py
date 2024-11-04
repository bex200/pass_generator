def numbers_and_calculation():
    numbers = []

    with open("numbers.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            numbers.append(number)

    total = sum(numbers)
    avg = sum(numbers) / len(numbers)
    maximum = max(numbers)

    print(total)
    print(avg)
    print(maximum)

numbers_and_calculation()
