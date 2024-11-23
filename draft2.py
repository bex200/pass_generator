class Animal:
    def __init__(self, name, species, age, is_endangered=None):
        self.name = name 
        self.species = species
        self.age = age 
        self.is_endangered = is_endangered or False

    def food_preference(self):
        if self.species == "wild":
            print(f'{self.name} is a wild animal and prefers eating a meat. It is {self.age} years old.')
        else:
            print(f'{self.name} is not wild animal and prefers not eating a meat. It is {self.age} years old.')

    def long_sleep(self):
        if self.age > 5:
            print(f'{self.name} is an old animal so that is why it sleeps longer than young ones.')
        else:
            print(f'{self.name} is a young animal so that is why its sleeping time takes less.')
    
first_animal = Animal("lion", "wild", 20)
# first_animal.food_preference()
# first_animal.long_sleep()

class Lion(Animal):
    def __init__(self, name, species, age, is_endangered=None):
        super().__init__(name, species, age, is_endangered)
        self.speed = 50

    def make_sound(self):
        print(f'{self.name} make a roar sound. Roaring is a way to gauge strength.')
    
    def hunting(self):
        print(f'{self.name} is one of the fastest animal with a top speed of about {self.speed} miles per hour.')

    def __str__(self):
        return  f'{self.name}, {self.species}, {self.age}'

lion_par = Lion("lion", "wild", 20)
# lion_par.make_sound()
# lion_par.hunting()

class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals_list = []

    def add_animal(self, animal_obj: Animal):
        self.animals_list.append(animal_obj)
        print(f'{animal_obj.name} is added to Exhibit {self.name}')

    def remove_animal(self, animal_obj: Animal):
        if animal_obj in self.animals_list:
            self.animals_list.remove(animal_obj)
            print(f'{animal_obj.name} is removed from Exhibit {self.name}')
        else:
            print('No such animal found!!!! ERROR')

    def show_animals(self):
        for animal in self.animals_list:
            print(animal)
    
    def __str__(self):
        return  f'{self.name}, {self.species}, {self.location}'

        print(self.animals_list)

exhibit_for_lions = Exhibit(name='LIONS EXH', location='Turan 45')
# exhibit_for_lions.add_animal(first_animal)
# exhibit_for_lions.remove_animal(first_animal)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def add_employee(self, employee_exh: Exhibit):
        print(f'{self.name} takes care of animals in the next exhibit: {employee_exh.location}.')

    def takes_care(self, animal: Animal):
        if self.position == "vet":
            print(f'{self.name} as a {self.position} is responsible for taking care of {animal.name}.')
        else:
            print(f'{self.name} as a zookeeper feeds a {animal.name} and responsible for their environment.')

    def daily_operations(self, animal: Animal):
        if self.position == "vet":
            print(f'{animal.name} get a balanced and nutritious diet that is prepared by {self.name}.')
        else:
            print(f'{self.name} feeds a {animal.name} every 8 hours.') 

employee_1 = Employee(name = "Jasmine", position = "vet")
employee_1.add_employee(exhibit_for_lions)
employee_1.takes_care(first_animal)
employee_1.daily_operations(first_animal)
employee_2 = Employee(name = "Jack", position = "zookeeper")
employee_2.add_employee(exhibit_for_lions)
employee_2.takes_care(first_animal)
employee_2.daily_operations(first_animal)