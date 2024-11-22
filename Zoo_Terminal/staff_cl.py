import time
from constants import TASKS, SATISFACTION, HEALTH_STATUS
from utilities import choose_random
import animal_cl


class Staff:
    def __init__(self, name, age):
        self.name = name
        self.position = ""
        self.age = age

    def __str__(self):
        return f"{self.name}, the {self.position}, {self.age} years old."

    def work(self):
        task = choose_random(TASKS)
        print(f"{self.name} {task}")

    def report(self, Exhibit):
        inhabitants = ""
        for Animal in Exhibit.animals:
            inhabitants += f"{Animal}. "
        print(f"=====Report from {self.name}, {self.position}=====\n"
              f"Exhibit: {Exhibit.name}\n"
              f"=====Info About Exhibit=====\n"
              f"Location: {Exhibit.location}\n"
              f"Inhabitants: {inhabitants}\n")

class Zookeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.position = "Zookeeper"

    def feed(self, animal, food):
        print(f"{self.name} is feeding {food} to {animal.name}, the {animal.species}")
        time.sleep(1)
        print(f"{animal.eat(food)}...")
        time.sleep(1)
        print(f"{animal.name} {choose_random(SATISFACTION)}")

class Vet(Staff):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.position = "Vet"

    def check_health(self, animal):
        print(f"{self.name} is checking health of {animal.name}, the {animal.species}")
        time.sleep(1)
        print(f"{self.name} is concentrated at their work...")
        time.sleep(1)
        print(f"INFO: \n\t{animal.info()}, \n\t\talso {choose_random(HEALTH_STATUS)}")




