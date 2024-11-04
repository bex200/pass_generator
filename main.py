# first_number = int(input('Введите первую цифру: '))
# operation = input('Введите операцию: ')
# second_number =  int(input('Введите вторую цифру: '))
#
# if operation == '+':
#     print('Ответ: ', (first_number + second_number))
# elif operation == '-':
#     print('Ответ: ', (first_number - second_number))
# elif operation == '*':
#     print('Ответ: ', (first_number * second_number))
# elif operation == '/':
#     if second_number != 0:
#         print('Ответ: ', (first_number / second_number))
#     else:
#         print('Деление на ноль! Нельзя так.')
# elif operation == '%':
#     print('Ответ: ', (first_number * second_number) / 100)
# elif operation == 'Квадрат':
#     print('Ответ: ', (first_number ** second_number))
# else:
#     print('Неправильная операция')


operacia = input('Введите вычисление, Например: 2+2 или 2*2:')
result = eval(operacia)

print(result)