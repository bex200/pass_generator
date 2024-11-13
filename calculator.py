from tkinter import *

FONT = ('Arial',16,'normal')
IS_OPERATION_SET = False
# ------------------- getting numbers -----------------------#
def press_numb(button_text):
    global first_numb
    global oper
    global display_text
    global second_numb
    if oper != '' and oper in display_text:
        second_numb += button_text
        display_text += button_text
        canvas.itemconfig(display,text=display_text)
    else:
        first_numb += button_text
        display_text += button_text
        canvas.itemconfig(display,text=display_text)
    return button_text

# ------------------- identifying operation -----------------#
def press_operation(operation):
    global oper
    global display_text
    global IS_OPERATION_SET
    if not IS_OPERATION_SET:
        display_text += operation
        IS_OPERATION_SET = True
    else:
        display_text = display_text.replace(oper,operation)
    oper = operation
    canvas.itemconfig(display,text=display_text)
    return operation


# ------------------- setting up UI----------------#
window = Tk()
window.config(bg='grey')
window.title("Calculator")
window.config(pady=20, padx = 20)

first_numb = ''
operation = ''
second_numb = ''

canvas = Canvas(width=100, height=50)
display = canvas.create_text(75,25,text='',font=('Arial',20,'normal'))
canvas.grid(column=0,row=0,columnspan=4,sticky='EW',padx=10,pady=10)

display_text = canvas.itemcget(display,'text')

one = Button(text='1', font=FONT, background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('1'))
two = Button(text='2', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('2'))
three = Button(text='3', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('3'))
four = Button(text='4', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('4'))
five = Button(text='5', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('5'))
six = Button(text='6', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('6'))
seven = Button(text='7', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('7'))
eight = Button(text='8', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('8'))
nine = Button(text='9', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('9'))
zero = Button(text='0', font=FONT,background=NUMB_COLOR,width=3,height=2, command=lambda: press_numb('0'))

plus = Button(text='+',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('+'))
subtract = Button(text='-',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('-'))
multiply = Button(text='*',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('*'))
divide = Button(text='/',font=FONT,background=OPER_COLOR,width=3,height=2, command=lambda:press_operation('/'))

float_numb = Button(text='.',font=FONT,width=3,height=2)
equal = Button(text='=',font=FONT,width=3,height=2)

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

# First version
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
