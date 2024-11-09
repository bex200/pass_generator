def calculator():
    history = []  # List to store the history of calculations

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation (a^b)")
        print("6. Modulus (a % b)")
        print("7. View History")
        print("8. Exit")

        choice = input("What operation do you want to choose? ")

        # Exit option
        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            # history.clear()
            break

        # View history option
        if choice == '7':
            if history:
                print("\nHistory of calculations:")
                for entry in history:
                    print(entry)
            else:
                print("No calculations yet.")
            continue

        # Validate the choice input
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please choose a number between 1 and 8.")
            continue

        try:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        # Perform calculation based on choice
        if choice == '1':
            result = a + b
            operation = f"The sum of {a} and {b} is: {result}"
        elif choice == '2':
            result = a - b
            operation = f"The difference of {a} and {b} is: {result}"
        elif choice == '3':
            result = a * b
            operation = f"The product of {a} and {b} is: {result}"
        elif choice == '4':
            if b == 0:
                print("Error: Division by zero is undefined.")
                continue
            else:
                result = a / b
                operation = f"The division of {a} by {b} is: {result}"
        elif choice == '5':
            result = a ** b
            operation = f"{a} raised to the power of {b} is: {result}"
        elif choice == '6':
            result = a % b
            operation = f"The modulus of {a} and {b} is: {result}"

        print(operation)
        history.append(operation)

# Run the calculator
calculator()

git remote add origin https://github.com/dannyocean21/Calculator.git
