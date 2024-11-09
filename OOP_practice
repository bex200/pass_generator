class Sotrudnik:
    def __init__(self,name,job_title, salary:int):
        self.name = name
        self.job_title = job_title
        self.salary = salary
    
    def introduce(self):
        print(f"Меня зовут {self.name}, моя должность - {self.job_title} с зарплатой {self.salary}$")

class Manager(Sotrudnik):
    def __init__(self, name, job_title, salary:int, bonus:int):
        super().__init__(name, job_title, salary)
        self.bonus = bonus
        
    def add_bonus(self):
        self.salary = self.salary + self.bonus
        return self.salary


class Developer(Sotrudnik):
    def __init__(self, name, job_title, salary: int, award: int):
        super().__init__(name, job_title, salary)
        self.award = award
        
    def add_award(self):
        self.salary = self.salary + self.award
        return self.salary


sotrudnik1 = Sotrudnik("Миша", "Сотрудник", 5000)
sotrudnik1.introduce()

sotrudnik2 = Manager("ВИктор","Менеджер", 5000, 4000)
sotrudnik2.add_bonus()
sotrudnik2.introduce()    

sotrudnik3 = Developer("Дима", "Разработчик", 5000, 6000)
sotrudnik3.add_award()
sotrudnik3.introduce()