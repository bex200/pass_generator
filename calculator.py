from tkinter import *
from webbrowser import open_new
# ------------------- identifying which button was clicked -----------------------#
def press_numb(button_text):
    global first_numb
    first_numb += button_text
    canvas.itemconfig(display,text=first_numb)
    return button_text

# ------------------- identifying operation -----------------#
def press_operation(operation):
    print(operation)


# ------------------- setting up UI----------------#
window = Tk()
window.title("Calculator")
window.config(pady=20, padx = 20)

first_numb = ''
operation = ''

canvas = Canvas(width=100, height=50)
canvas.create_text(50,25,text='text',font=('Arial',30,'normal'))
canvas.grid(column=0,row=0,columnspan=4,sticky='EW')

one = Button(text='1')
two = Button(text='2')
three = Button(text='3')
four = Button(text='4')
five = Button(text='5')
six = Button(text='6')
seven = Button(text='7')
eight = Button(text='8')
nine = Button(text='9')
zero = Button(text='0')
plus = Button(text='+')
subtract = Button(text='-')
multiply = Button(text='*')
divide = Button(text='/')
float_numb = Button(text='.')
equal = Button(text='=')

equal.grid(column=0,row=4)
float_numb.grid(column=2,row=4)
zero.grid(column=1,row=4)
one.grid(column=0,row=3)
two.grid(column=1,row=3)
three.grid(column=2,row=3)
four.grid(column=0,row=2)
five.grid(column=1,row=2)
six.grid(column=2,row=2)
seven.grid(column=0,row=1)
eight.grid(column=1,row=1)
nine.grid(column=2,row=1)
plus.grid(column=3,row=4)
subtract.grid(column=3,row=3)
multiply.grid(column=3,row=2)
divide.grid(column=3,row=1)





window.mainloop()

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
