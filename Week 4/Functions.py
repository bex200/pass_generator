# Imagine you want to cook different meals for party
# functions will help you to write the recipe,
# so you will not write it many times

#Funstion - is a block of code that does the particlular task
#def use that to create

#Example:
def greet_first():
    print("Hellp world")

# We can call the function, by just saying its name with paranthesis
# when you use "greet()", programm will run the code inside the function b will return "Hello world"
greet_first()

# Sometimes we need to use some of our own information, so it will
#run the code parameters - are the variables when we create a function
#Example
def greet(name):
    print(f"Hello, {name}!")

greet("Bekzat") # Bekzat is the argument of the function

#Functions are not only for running the block of code or to complete
# the particular action, but to return the value as well
# for that we need to return the word return should be used

def add(a, b):
    return a+b

result_of_sum_function = add(4,5)
print(result_of_sum_function)
# Now when I call the add(3,5) function will return 8
# we can use it for variable



