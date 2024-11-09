# == Topic: why we need OOP and what is object ===

# OOP (Object oriented programming) helps us organize the programming,
# it is more of a style
# Joint database and action into one whole structure, and is called object
# Without OOP we coundn't use much of the разненных что было бы сложно поддержать,


# What is object?
# Imagine urself, that every person in the family is object. Each of the person has a data (name, age)
# And the actions (For example, he can do for example cooking, working, teach kids)
# in OOP, object joints this data in one place, and works like a folder for each member of the family

# Example of the object "human", who has name, age, method, to introduce themselves.


# Object elements
# Object consists of 2 main components:
# 1. Attribute - data, which describes the object (for example age)
# 2. Method - action, which can do certain thing (introduce urself)

# Example:
# 1. Attribute: name, age
# 2. Method: introduce

class Person: # Creates an object which includes an attribute and method at the same place capital letters
    #* Constructor: initialize object with data (name, age) WE NEED IT НАМ НУЖЕН ЧТОБЫ МОМЕНТАЛЬНО ПРИДАВАТЬ ЧЕЛОВЕКУ ОПР. ЗНАЧЕНИЯ
    def __init__(self, name, age): # self shows that function init is related to Person
        self.name = name # Attribute: name
        self.age = age   # Attribute: age

    # Method: thing that object can do
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old!"

# Why do we create object?
# If there were no OOP, we would have stored the information about the person in different places
# Name, age, action - everything would be in different palces and it would have been hard for processing

# OOP allows sort all the data and actions in one place - object
#This help to work with data, because we can operate with objects

dad = Person("John", 45)

# print(dad.age)
# print(dad.name)

# print(dad.introduce())





