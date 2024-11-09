# What is init and why do we need it?

# Imagine, that you created your friend, for example "Ivan"
# You want that he had a name and age. But what if, you want to create many other friends, with different names?

#For example you would have written this:
class Person:
    name= ""  #Empty name by default
    age = 0   #Empty age by default

# Now imagine , if you want to create a person, with specific name and age, you could have written:
friend1 = Person()
friend1.name = "Ivan" #Given name
friend1.age = 25 #Given age

friend2 = Person() # Create one more person
friend2.name = "Maria"
friend2.age = 30

#It works
# Это работает, но представь, если бы тебе нужно было каждый раз отдельно ставить имя и возраст каждому человеку.
# Это неудобно, особенно если людей много, и каждый раз ты бы вручную прописывал эти значения.

# This is why we need init:
# This command instantly helps create object and give the, a value needed for data(Example name and age) and do not do manually

#so we can write it like this:
class Person:
    def __init__(self, name, age, email): # for class it is method
        # Here we instantly create person and give a value to variables
        self.name = name
        self.age = age
        self.email = email
    def list_of_all(self):
        print(self.name, self.age, self.email)
    def add_one_to_age(self):
        self.age = self.age + 1
        print(f"New age after birthday is {self.age}")
# Now we can create person, and you can just give value to it:
friend1= Person("Ivan", 45, "example@gmail.com")
friend2= Person("Maria", 30, "masha@ru.ru")

list_of_people = [friend1, friend2]

# You are not obliged to write by hand name and age after creating object, everything is done instantly
print(friend1.name)
friend1.list_of_all()
friend1.add_one_to_age()
print(list_of_people)

# Instance of classes are friend1 and friend2



