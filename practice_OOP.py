class Employee:
    def __init__(self, name, job, bs):
        self.name = name
        self.job = job
        self.bs = bs
    def intro(self):
        print(f'Сотрудник {self.name} имеет должность {self.job} и получает {self.bs} долларов')


class Managers(Employee):
    def __init__(self, name, job, bs, bonus):    
        super().__init__(name, job, bs)
        self.bonus = bonus
    def salary_job(self):
        self.sj = self.bonus + self.bs
        return self.sj
    def intro(self):
        print(f'Сотрудник {self.name} имеет должность {self.job} и получает {self.salary_job()} долларов')

class Developers(Employee):
    def __init__(self, name, job, bs, prize):
        super().__init__(name, job, bs)
        self.prize = prize
    def salary_job(self):
        self.pj = self.prize + self.bs
        return self.pj
    def intro(self):
        print(f'Сотрудник {self.name} имеет должность {self.job} и получает {self.salary_job()} долларов')

Managers('Джон', 'менеджер', 100, 15).intro()
Developers('Стив', 'разработчик', 500, 30).intro()



