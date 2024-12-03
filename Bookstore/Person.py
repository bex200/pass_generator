from DatabaseManager import DatabaseManager

db = DatabaseManager("bookstore.db")  # Подключаемся к базе данных.

class Person:
    def __init__(self, title):
        self.title  = title
        self.author = ""
        self.year = "2024-01-01"
        self.genre = ""
        self.price = 0
        self.amount = 0

        def buy_book(self, amount, title):
            db.update_data("books", amount, title)