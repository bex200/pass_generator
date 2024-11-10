class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Создаем объект банковского счета
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
