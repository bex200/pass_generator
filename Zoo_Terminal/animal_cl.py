import time


class Animal:
    def __init__(self, name, age, is_endangered):
        self.name = name
        self.species = ""
        self.age = age
        self.is_endangered = bool(is_endangered)

    def make_sound(self):
        print("#ABSTRACTION TEMPLATE. NOT TO BE CALLED#")

    def eat(self, food):
        print(f"{self.name}, the {self.species}, is eating {food}")

    def sleep(self):
        print(f"{self.name}, the {self.species}, is currently sleeping")


class Lion(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, age, is_endangered)
        self.species = "Lion"

    def make_sound(self):
        print(f"'RAWR' (c) {self.name}, the {self.species}.")

    def info(self):
        print(f"{self.name}, the {self.species}, is {self.age} and "
              f" {"is Endangered" if self.is_endangered else "is not Endangered"}.")

    def assert_dominance(self):
        print(f"{self.name}, the {self.species}, giving out his most powerful growl to state his dominance")

    def __str__(self):
        return f"{self.name}, the {self.species}"

class Monkey(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, age, is_endangered)
        self.species = "Monkey"

    def make_sound(self):
        print(f"'Uooa Uaooo' (c) {self.name}, the {self}")  # Lmao

    def info(self):
        print(f"{self.name}, the {self.species}, is {self.age} and "
              f" {"is Endangered" if self.is_endangered else "is not Endangered"}")

    def grapple_tricks(self):
        print(f"{self.name}, the {self.species} is swinging from tree to tree, doing back flips")

    def __str__(self):
        return f"{self.name}, the {self.species}"

class Penguin(Animal):
    def __init__(self, name, age, is_endangered):
        super().__init__(name, age, is_endangered)
        self.species = "Penguin"

    def make_sound(self):
        print(".", end=" ")
        time.sleep(0.5)
        print("..", end=" ")
        time.sleep(0.75)
        print("...", end=" ")
        time.sleep(1)
        print(f"(с) {self.name}, the {self.species}. Penguins are not talking.")

    def info(self):
        print(f"{self.name}, the {self.species}, is {self.age} and "
              f"{'is Endangered' if self.is_endangered else "is not Endangered"}")

    def swim(self):
        print(f"{self.name}, the {self.species} is swimming in icy water, seemingly relaxed.")

    def __str__(self):
        return f"{self.name}, the {self.species}"