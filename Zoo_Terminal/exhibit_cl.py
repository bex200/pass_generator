
class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []

    def add_animal(self, Animal):
        self.animals.append(Animal)

    def remove_animal(self, Animal):
        self.animals.remove(Animal)

    def show_all_animals(self):
        print(f"In exhibit {self.name} (located in {self.location}), there are {len(self.animals)} animals:", end=" ")
        for animal in self.animals:
            print(animal, end=". ")
        print("")

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}"