#First part
class Employee:
    def __init__(self, name, position, base_salary):
        self.name = name  
        self.position = position
        self.base_salary = base_salary    

    def introduce(self):  
        return f"{self.name} работает на должности {self.position} и получает оклад в размере {self.base_salary} тенге."
    
first_employee = Employee("Arman", "Manager", 2000)
#print(first_employee.introduce()) 


#Second part + additional employee
class Manager(Employee):
    def __init__(self, name, position, base_salary, bonuses):
        super().__init__(name, position, base_salary) 
        self.bonuses = bonuses   

    def total_salary(self):
        self.base_salary =  int(self.base_salary) + int(self.bonuses)
        print(f'Размер его бонусов равен {self.bonuses} тг. Его итоговая зарплата вместе с бонусами составляет {self.base_salary}.')    

first_manager = Manager("Arman", "Manager", 4000, 7000)
second_manager = Manager("Esbol", "Manager", 5000, 6500)

print(first_manager.introduce()) 
print(first_manager.total_salary()) 
print(second_manager.introduce()) 
print(second_manager.total_salary()) 

#Third part + additional employee
class Developer(Employee):
    def __init__(self, name, position, base_salary, bonuses):
        super().__init__(name, position, base_salary) 
        self.bonuses = bonuses   

    def total_salary(self):
        self.base_salary =  int(self.base_salary) + int(self.bonuses)
        print(f'Размер его бонусов равен {self.bonuses} тг. Его итоговая зарплата вместе с бонусами составляет {self.base_salary}.')    

first_dev = Developer("Diana", "Developer", 5400, 3600)
second_dev = Developer("Artem", "Developer", 7800, 5300)
print(first_dev.introduce()) 
print(first_dev.total_salary())
print(second_dev.introduce()) 
print(second_dev.total_salary())
