class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Создаем объекты Dog и Cat
dog = Dog()
cat = Cat()

dog.speak()  # Woof!
cat.speak()  # Meow!
