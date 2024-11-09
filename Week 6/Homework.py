# Homework - Mashirapov Darkhan
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def DisplayName(self):
        return f"My name is {self.name}, "

    def DisplayPosition(self):
        return f"I currently work as {self.position} at company ABC, "

    def total_salary_earned(self):
        return f"My salary is {self.salary} KZT per month, "

#1. When bonus is based on salary
class Manager1(Employee):

    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
    def bonus(self):
        return int(self.salary * 0.15)

    def total_salary_earned(self):
        total_salary = self.salary + self.bonus()
        return f"My salary is {total_salary} KZT per month because it is based on my salary"

#2. When bonus is input
class Manager2(Employee):
    def __init__(self, name, position, salary, bonus):
        super().__init__(name, position, salary)
        self.bonus = bonus

    def total_salary_earned(self):
        total_salary = self.salary + self.bonus
        return f"My salary is {total_salary} KZT per month because it is a fixed amount"


class Developer(Employee):
    def __init__(self, name, position, salary, compensation):
        super().__init__(name, position, salary)
        self.compensation = compensation

    def total_salary_earned(self):
        total_salary = self.compensation + self.salary
        return f"My salary is {total_salary} KZT per month, because it depends on the projected completed"

# Creating instances
manager1 = Manager1("Aiym", "Manager", 1000000)
manager2 = Manager2("Darkhan", "Manager", 1000000, 150000)
developer = Developer("Bekzat", "Developer", 900000, 140000)

# Displaying the results
print(manager1.DisplayName() + manager1.DisplayPosition() + manager1.total_salary_earned())
print(manager2.DisplayName() + manager2.DisplayPosition() + manager2.total_salary_earned())
print(developer.DisplayName() + developer.DisplayPosition()  + developer.total_salary_earned())

# continue allows us to immediately skip the remaining code in the current
# #iteration of the loop and restart the loop for another valid input.
for i in range(5):
    if i == 2:
        continue
    print(i)
