import constants as const


class Customer:
    def __init__(self, bookstore):
        self.bookstore = bookstore
        self.cart = []

    def show_cart(self):
        for book in self.cart:
            print(f'\t{book}')

    def buy_book(self, condition, amount):
        book = self.bookstore.get_book(const.TABLE_NAME, condition)

        if not book:
            print("❌ Book not found.")
            return

        book_details = book[0]
        title, author, year, genre, price, available_amount = book_details

        if amount > available_amount:
            print(f"❌ Not enough stock. Available: {available_amount}, Requested: {amount}.")
            return

        remaining_amount = available_amount - amount
        update_condition = f"title = '{title}'"
        update_data = f"amount = {remaining_amount}"

        self.bookstore.update_book(const.TABLE_NAME, update_data, update_condition)
        print(
            f"✅ Purchase successful! You bought {amount} copy(ies) of '{title}'. Remaining stock: {remaining_amount}.")
        self.cart.append([title, author, year, genre, price, amount])

    def search_book(self):
        print(f"Search for a book by:\n\t1. Title\n\t2. Author\n\t3. Year\n\t4. Genre\n\t")

        try:
            choice = input("Enter the number corresponding to your choice: ")

            if choice not in const.SEARCH_FIELDS:
                print("❌ Invalid choice. Please try again.")
                return

            field = const.SEARCH_FIELDS[choice]
            query_value = input(f"Enter the {field} to search for: ")

            condition = f"{field} LIKE '%{query_value}%'"
            results = self.bookstore.get_book(const.TABLE_NAME, condition)

            if not results:
                print(f"❌ No books found for {field}: {query_value}.")
                return

            while len(results) > 1:
                print("Multiple books found:")
                for idx, book in enumerate(results, start=1):
                    print(f"{idx}. {book}")

                selection = input("Enter the number of the book you want to select, or refine your search: ")

                if selection.isdigit():
                    selection = int(selection)
                    if 1 <= selection <= len(results):
                        selected_book = results[selection - 1]
                        print(f"✅ You selected: {selected_book}")
                        return selected_book
                    else:
                        print("❌ Invalid selection. Please try again.")
                else:
                    print(f"Refining search by {field}: {selection}")
                    condition = f"{field} LIKE '%{selection}%'"
                    results = self.bookstore.get_book(const.TABLE_NAME, condition)

            if len(results) == 1:
                selected_book = results[0]
                print(f"✅ You selected: {selected_book}")
                return selected_book
        except Exception as e:
            print(f"❌ Invalid input. ERROR: {e}.")
