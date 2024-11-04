# def plus(a,b):
#     return a+b

# x= 4
# y = 10 
# print(plus(x,y))


# Example 2
# def my_function(a,b,c):
#     print("The value of a is: " + a)
#     print("The value of b is: " + b)
#     print("The value of c is: " + c)

# my_function(a="Emil", b="Tobias", c="Linus")

# Example 3
# def calculate(a,b):
#     return a+b, a-b, a*b
# sum, diff, mult = calculate(3,4)
# d = sum, diff, mult
# print(d)

#Example 4 - рекурсивная функция вызывает саму себя 
# пока не закончит с самой с собой 
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))

# #Example 5
# def power(base, exponent):
#     return base**exponent
# print(power(exponent=3, base=2))

# Функции как обьекты первого класса
# def add(a,b):
#     return a+b
# def operate(func, x, y): # x and y are arguments
#     return func(x,y)
# print(operate(add, 3,4))

