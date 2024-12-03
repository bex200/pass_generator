from DatabaseManager import DatabaseManager

db = DatabaseManager("bookstore.db")  # Подключаемся к базе данных.

# Создаём таблицу.
db.create_table(
    table_name="books",
    columns={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT",
        "author": "VARCHAR(255)",
        "year": "DATE",
        "genre ": "TEXT",
        "price": "REAL",
        "amount": "INTEGER"
    }
)


class Bookstore:
    def __init__(self, title,author, year, genre, price, amount):
        self.title  = title
        self.author = author
        self.year = year
        self.genre = genre
        self.price = price
        self.amount = amount

    def add_new_book(self, title,author, year, genre, price, amount):
        db.insert_data(
            table_name="books",
            data= [
                (None, title,author, year, genre, price, amount ),
            ]
        )
    def delete_book(self, title):
        db.delete_data("books", title)


    def update_book(self, updates, condition):
        db.update_data("books", updates, condition)

    def select_book(self, condition):
        db.fetch_by_condition("books", condition)

    def select_all_book(self):
        db.fetch_all("books")