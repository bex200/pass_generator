# Imagine you want to collect the instrument for you hobbie
# Each intrument has its ourpose
# In programming the module - is a collection of the instruments, which contains functions, variables for
#the purpose of completing certain tasks
# Packages - it is group of modules, which helps

# Module is the code file in Python, that contains fucntion, casses and variables
# In order to use it we need to import it
# In python there are inside

import math
# Now we can use functions from module math in other functions

def calculate_square_root(number):
    return math.sqrt(number)

def calculate_area_of_circle(radius):
    return math.pi*(radius**2)

def round_any_number(number):
    return round(number)

root_result =  calculate_square_root(16)
area_result = calculate_area_of_circle(5)
rounded_number = round_any_number(1.223445645)

print(f"Rounded result of 1.2334345 is {rounded_number}")
print(f"Square root of 16: {root_result}")
print(f"Area of the circle with radius of 5: {area_result}")

def round_to_floor(number):
    return math.floor(number)
def round_to_ceil(number):
    return math.ceil(number)

print(round_to_ceil(1.78))

# Packages - is a way to organize a module into one folder, so it will be easier to manage
#Pazkages allow us create hierarchy of modules, which helps to