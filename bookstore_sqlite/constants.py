TABLE_NAME = "bookstore_table"

COLUMNS = {
    "title": "TEXT",
    "author": "VARCHAR(255)",
    "year": "DATE",
    "genre": "TEXT",
    "price": "REAL",
    "amount": "INTEGER"
}

DATA = [
    ("Do android dream of electric sheep", "Angela", 2021, "sci-fi", 1000, 1),
    ("Orlando furioso", "Roland", 2012, "tragedy", 1000, 24),
    ("Funeral of dead butterflies", "Yesod", 1921, "requiem", 1000, 10),
    ("Love town", "Tomery", 2011, "horror", 1000, 14),
    ("Crying children", "Phillip", 2022, "drama", 1000, 16),
    ("Will of the city", "Yan", 2003, "folklore", 1000, 111),
    ("Iron Lotus", "Xiao", 2019, "drama", 1000, 3),
    ("Blue reverberation", "Argalia", 2023, "modern", 1000, 9)
]


SEARCH_FIELDS = {
                    "1": "title", "t": "title", "-t": "title",
                    "2": "author", "a": "author", "-a": "author",
                    "3": "year", "y": "year", "-y": "year",
                    "4": "genre", "g": "genre", "-g": "genre"
                }

THE_WORST_IMPLEMENTATION_OF_LOGIN = {
    "admin": "admin",
    "milterdone": "mtd1"
}

MENU_OPTIONS = {
    "1": "add_book", "add book": "add_book", "add": "add_book", "ab": "add_book", "a": "add_book",
    "2": "delete_book", "delete book": "delete_book", "delete": "delete_book", "db": "delete_book", "d": "delete_book",
    "3": "update_book", "update book": "update_book", "update": "update_book", "ub": "update_book", "u": "update_book",
    "4": "search_book", "search book": "search_book", "search": "search_book", "sb": "search_book", "s": "search_book",
    "5": "purchase_book", "purchase book": "purchase_book", "purchase": "purchase_book", "pb": "purchase_book", "p": "purchase_book",
    "6": "exit", "exit": "exit", "q": "exit", "e": "exit",
    "7": "login", "login": "login", "l": "login", "log": "login"
}
