# Imagine that you have all the ingredients for cooking
# But suddenly you realise you don't have the essial element '
# Example: we can use try-except:

# Кодировка utf-8
# We use utf-8 is standard coding, which allows works with text


# 1. try except in Python
# 2. Exceptions are the errors which appears when we run the program
# 3. By using the except, we can catch that errors and continue running the program
# Examples: ZeroDivisionError, FileNotFound, ValueError

def divide_without_try():
    number = int(input("Enter a number: "))
    divide_10 = 10 / number
    print(round(divide_10))
    print("You see this if there is no error, if not program dies")

# divide_without_try()

# Example 1: Using try and except

def divide_numbers():
    try:
        number = int(input("Enter a number: "))
        divide_10 = 10 / number
        print(round(divide_10))
    except ZeroDivisionError:
        print("Error: can't divide by 0")
    except ValueError:
        print("Error: use numbers! ")
    print("Even after some errors our code work") # This will run because we skip the errors, and it will be in the output

# while True:
#     divide_numbers()


# Example 2: Reading file with processing the exceptions
def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read() # reading the content
    except FileNotFoundError: # If file does not exist
        print("Error: file not found")
    except PermissionError: # Don't have the rights
        print("Error: we don;t have access")
    except Exception as e: #General error
        print(f"Error occurred: {e}") # Print the message about the error
    finally: # It will run even though we forgot to mention some of th error type
        print("Finish the work of the function read_file.")

# Run the function with non existing name
# read_file("non_existing_file.txt")

# Example 3: processing the exception while working with lists

def list_example():
    my_list =[1, 2, 3]
    try:
        index = int(input("Input the index for accessing in range(0-2): "))
    except IndexError:
        print("Out of range")
    except ValueError:
        print("Incorrect")

# raise is a key word that goes with try and except
import math
def calculate_sqrt():
    try:
        number = float(input("Enter a number for calculating the square root: "))
        if number < 0:
            raise ValueError("Square root of negative number does not exist")
        result = math.sqrt(number)
        print("Square root:", result)
    except ValueError as we:
        print("Error: ", we)

