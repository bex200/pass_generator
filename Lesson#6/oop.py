class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

# Создаем объекты (машины) на основе класса Car
car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")

car1.drive()  # The red Toyota is driving.
car2.drive()  # The blue BMW is driving.
