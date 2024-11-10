class Bird:
    def fly(self):
        print("Flying in the sky")

class Penguin(Bird):
    def fly(self):
        print("I can't fly, I swim!")

# Функция, использующая полиморфизм
def make_bird_fly(bird):
    bird.fly()

sparrow = Bird()
penguin = Penguin()

make_bird_fly(sparrow)  # Flying in the sky
make_bird_fly(penguin)  # I can't fly, I swim!
