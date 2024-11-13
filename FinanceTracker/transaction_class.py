import datetime

class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today()


    def display (self):
        if self.amount >= 0:
            sign = '+'
        else:
            sigh = '-'

        amount_str = f"${abs(self.amount)}"

        return f"{self.date} - {self.category}: {sign}{amount_str}"