
#* Модуль — это файл с кодом на Python, который может содержать функции, классы и переменные. 
#* Чтобы использовать функции из модуля, вам нужно его импортировать. 
#* В Python существует много встроенных модулей, например, модуль `math`, который содержит математические функции и константы.

import math

#? Теперь вы можете использовать функции из модуля math в других функциях:

def calculate_square_root(number):
    return int(math.sqrt(number))

def calculate_area_of_circle(radius):
    return math.pi * (radius ** 2)

def round_any_number(number):
    return round(number)

def round_to_floor(number):
    return math.floor(number)

def round_to_ceil(number):
    return math.ceil(number)

print(round_to_floor(1.7))
print(round_to_ceil(1.1))

# Пример использования функций
root_result = calculate_square_root(16)
circle_area_result = calculate_area_of_circle(5)
rounded_number = round_any_number(1.7)

# print(f'Результат округления из 1.7: {rounded_number}')

# print(f"Квадратный корень из 16: {root_result}")  # Вывод: Квадратный корень из 16: 4.0
# print(f"Площадь круга с радиусом 5: {circle_area_result}")  # Вывод: Площадь круга с радиусом 5: 78.53981633974483

#* Использование функций модуля**: 
#   - В функции `calculate_square_root` мы возвращаем квадратный корень числа, используя функцию `sqrt` из модуля `math`. 
#   - В функции `calculate_area_of_circle` мы вычисляем площадь круга, используя `math.pi`.




# Пакет — это способ организовать связанные модули в одну папку, чтобы было легче управлять ими. 
# Пакеты позволяют создавать иерархии модулей, что помогает избежать конфликтов имён и делает код более структурированным.

#? LETS CREATE A PACKAGE🥳🥳🥳

# geometry/
#!     __init__.py
#     circle.py
#     rectangle.py
