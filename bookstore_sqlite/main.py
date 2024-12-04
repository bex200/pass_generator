import sqlite3
import constants as const
import utilities as util
import customer_cl as customer
import bookstore_cl as bookstore


def display_help():
    print("~-~-~-~-~ BOOKSTORE TERMINAL HELP ~-~-~-~-~")
    command_to_keys = {}

    for key, command in const.MENU_OPTIONS.items():
        command_to_keys.setdefault(command, []).append(key)

    for command, keys in command_to_keys.items():
        readable_command = command.replace('_', ' ').capitalize()
        keys_display = ", ".join(keys)
        print(f"{readable_command}:\n  Call: {keys_display}")


def login():
    print("\n[   Login   ]")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in const.THE_WORST_IMPLEMENTATION_OF_LOGIN and \
            const.THE_WORST_IMPLEMENTATION_OF_LOGIN[username] == password:
        print(f"✅ Welcome, {username}!")
        return True
    else:
        print("❌ Invalid login credentials.")
        return False


def add_book_to_store(bookstore):
    title = util.validate_alpha_input("Enter the book title: ")
    author = util.validate_alpha_input("Enter the author: ")
    year = util.validate_numeric_input("Enter the year of release: ")
    genre = util.validate_alpha_input("Enter the genre: ")
    price = float(util.validate_numeric_input("Enter the price: "))
    amount = util.validate_numeric_input("Enter the amount in stock: ")

    bookstore.add_book(const.TABLE_NAME, [(title, author, year, genre, price, amount)])


def delete_book_from_store(bookstore):
    title = util.validate_alpha_input("Enter the title of the book to delete: ")
    condition = f"title = '{title}'"
    bookstore.delete_book(const.TABLE_NAME, condition)


def update_book_in_store(bookstore):
    title = util.validate_alpha_input("Enter the title of the book to update: ")
    field = util.validate_alpha_input("Enter the field to update (price/amount): ").lower()
    if field not in ["price", "amount"]:
        print("Invalid field!")
        return
    value = util.validate_numeric_input(f"Enter the new value for {field}: ")
    updates = f"{field} = {value}"
    condition = f"title = '{title}'"
    bookstore.update_book(const.TABLE_NAME, updates, condition)


def search_book_in_store(customer):
    customer.search_book()


def purchase_book(customer):
    title = customer.search_book()
    amount = util.validate_numeric_input("Enter the amount to purchase: ")
    print(title)
    print(title[0])
    condition = f"title = '{title[0]}'"
    print(condition)
    customer.buy_book(condition, amount)


def main():
    print("[   Welcome to the Bookstore   ]")
    print("\nEnter 'Help' for a list of commands.")

    db_name = const.TABLE_NAME
    bookstore_instance = bookstore.Bookstore(db_name)
    bookstore_instance.create_table(const.TABLE_NAME, const.COLUMNS)
    bookstore_instance.add_book(const.TABLE_NAME, const.DATA)
    print("\n~~~~~ OUR ASSORTMENT ~~~~~\n")
    bookstore_instance.get_book(const.TABLE_NAME, 'year > 1')
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    customer_instance = customer.Customer(bookstore_instance)

    is_admin = False

    while True:
        choice = util.validate_choice("#BookStore> ", const.MENU_OPTIONS.keys())
        command = const.MENU_OPTIONS[choice]

        if command == "help":
            display_help()
        elif command == "login":
            is_admin = login()
        elif command == "add_book" and is_admin:
            add_book_to_store(bookstore_instance)
        elif command == "delete_book" and is_admin:
            delete_book_from_store(bookstore_instance)
        elif command == "update_book" and is_admin:
            update_book_in_store(bookstore_instance)
        elif command == "search_book":
            search_book_in_store(customer_instance)
        elif command == "purchase_book":
            purchase_book(customer_instance)
        elif command == "exit":
            print("Exiting the system. Goodbye!")
            bookstore_instance.close_connection()
            break
        elif choice in ["add_book", "delete_book", "update_book"] and not is_admin:
            print("❌ Admin privileges are required for this action. Please login.")
        else:
            print("❌ Invalid command. Please try again.")


if __name__ == "__main__":
    main()
