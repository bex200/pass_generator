def add(n1, n2):
    return n1 + n2

def subtract(a,b):
    return a - b

def multiply(c, d):
    return c * d

def divide(k, l):
    return k / l

maths = {
    '+' : add,
    '/' : divide,
    '-' : subtract,
    '*' : multiply
}

# print(maths['*'](4,8))
# my_favourite_calculation = add
# print(my_favourite_calculation(3, 5))
def calculator():
    contin = True
    first_numb = float(input('Please insert first number: \n'))
    while contin:
        oper = input('Choose the operation you want to trigger. Type *, -, + or /:\n')
        second_numb = float(input('Please insert second number: \n'))
        output = maths[oper](first_numb,second_numb)
        if output % 1 > 0:
            print(output)
        else:
            output = int(output)
            print(output)
        further = input(f'Would you like to continue with the result {output}? Type yes or no. \n')
        if further.lower() == 'yes':
            first_numb = output
        elif further.lower() == 'no':
            contin = False
        else:
            print('Invalid answer')
            break

calculator()