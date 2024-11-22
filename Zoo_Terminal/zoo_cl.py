import exhibit_cl
import staff_cl
import random
import utilities as util

class Zoo:
    def __init__(self):
        self.exhibits = []
        self.staff = []

    def add_exhibit(self, name, location):
        self.exhibits.append(exhibit_cl.Exhibit(name, location))

    def add_staff(self, position, name, age):
        if position == "Zookeeper":
            self.staff.append(staff_cl.Zookeeper(name, age))
        else:
            self.staff.append(staff_cl.Vet(name, age))

    def daily_operations(self):
        for staff in self.staff:
            staff.work()
            rand_exhibit = random.choice(self.exhibits)
            rand_animal = random.choice(rand_exhibit.animals)
            if staff.position == "Zookeeper":
                staff.feed(rand_animal)
            else:
                staff.check_health(rand_animal)

    def select_exhibit(self):
        if not self.exhibits:
            print("No exhibits available in the zoo.")
            return None

        while True:
            print("Select an exhibit:")
            for i, exhibit in enumerate(self.exhibits, start=1):
                print(f"\t{i}. {exhibit.name}")
            ex_index = util.validate_numeric_input("Enter the exhibit number: ") - 1

            if 0 <= ex_index < len(self.exhibits):
                exhibit = self.exhibits[ex_index]
                return exhibit
            else:
                print(f"Invalid exhibit number. Please select a number between 1 and {len(self.exhibits)}.")

    def select_an_animal(self):
        exhibit = self.select_exhibit()
        if exhibit is None:
            print("No exhibit selected. Operation canceled.")
            return None

        if not exhibit.animals:
            print(f"Exhibit '{exhibit.name}' has no animals.")
            return None

        while True:
            print("Select an animal:")
            for i, animal_exhibited in enumerate(exhibit.animals, start=1):
                print(f"\t{i}. {animal_exhibited}")
            animal_index = util.validate_numeric_input("Enter the animal number: ") - 1

            if 0 <= animal_index < len(exhibit.animals):
                return exhibit.animals[animal_index]
            else:
                print(f"Invalid animal number. Please select a number between 1 and {len(exhibit.animals)}.")