def divide_without_try():
    number = int(input("Enter the number "))
    divide_10 = 10/number  
    print(divide_10)
    print("You see me only if there are no mistakes, unless I die")

# divide_without_try()

def divide_without_number():
    try: 
        number = int(input("Enter the number "))
        result= 10/number  
        print("The result of division: ", result)
    except ZeroDivisionError:
        print("Error: you can't devide by zero")
    except ValueError:
        print("Error type the right number")
    print("Mistakes are just steps for a better result")

divide_without_number()