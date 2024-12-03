class Animal:

    def __init__(self, name, species, age, is_endangered=None):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered or False
        # self.__passwprd = "admin@adminov"
        # self._half_secret = "adminov"


    def make_sound(self):
        pass
        # print(f"{self.name} - {self.species} - MAKES THIS SOUND {sound}")

    def eat (self):
        pass
        # print(f"{self.species} - is eating {food}")

    def sleep (self):
        pass
        # print(f"{self.name} - {self.species} is sleeping")
        # return True



class Lion (Animal):

    def __init__(self, name, age, is_endangered=None ):
        super().__init__(name, "Lion", age,  is_endangered)
        self.speed = 80

    def make_sound(self):
        print(f"{self.name} is {self.species} makes this sound RRRR")

    def hunting(self):
        print(f"{self.species} with name {self.name} is hunting")

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}"

class Zebra (Animal):
    def __init__(self, name, age, is_endangered=None):
        super().__init__(name, "Zebra", age, is_endangered)
        self.has_stripes = True

    def make_sound(self):
        print(f"{self.name} {self.species} makes this sound feeeeaaarrrr")

    def run_from_lion (self, lion_obj: Lion):
        print(f"{self.species} {self.name} is running from {lion_obj.name}")
        lion_obj.hunting()

class Giraffe(Animal):
    def __init__(self, name, age, is_endangered=None):
        super().__init__(name, "Giraffe", age, is_endangered)
        self.neck_length = 2

    def make_sound(self):
        print(f"{self.name} - {self.species} MAKES THIS SOUND dfdfsfadf")

    def cures_animals (self, animal: Animal):
        print(f"{self.name} is curing  {animal.name} the {animal.species} ")
        animal.make_sound()


#
# animal_object = Animal ("Test Animal name", "Animal species", 10)
#
# test_lion_obj1 = Lion("Alex","Lion", 5)
# test_lion_obj2 = Lion("Simba","Lion", 3, True)
#
# test_lion_obj1.make_sound()
# test_lion_obj2.make_sound()
#
# test_lion_obj1.hunting()
# test_lion_obj2.hunting()
#
# test_zebra_object = Zebra ("Martin","Zebra", 4)
# test_zebra_object.run_from_lion(test_lion_obj1)
# test_zebra_object.make_sound()
#
#
# test_giraffe_object = Giraffe("Melmon","Giraffe",6)
# test_giraffe_object.cures_animals(test_lion_obj2)
# test_giraffe_object.cures_animals(test_zebra_object)
# test_giraffe_object.cures_animals(animal_object)
