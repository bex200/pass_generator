import sqlite3

class Bookstore:
    def __init__(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            print(f"✅ Connected to {db_name}")
        except sqlite3.Error as error:
            print(f"❌ Couldn't connect to {db_name}: {error}")

    def create_table(self, table_name, columns):
        try:
            column_definitions = ""
            for name, dtype in columns.items():
                column_definitions += f"{name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ")
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"✅ Table '{table_name}' created successfully.")
        except sqlite3.Error as error:
            print(f"❌ Error when creating the table: {error}")

    def add_book(self, table_name, data):
        try:
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "
            placeholders = placeholders.rstrip(", ")

            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data)
            self.connection.commit()
            print(f"✅ Book successfully added in '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Error when adding the book: {error}")

    def delete_book(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"✅ Data where '{condition}' successfully deleted from '{table_name}'.")
        except sqlite3.Error as error:
            print(f"❌ Error when deleting data: {error}")

    def update_book(self, table_name, updates, condition):
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            print(update_query)
            self.cursor.execute(update_query)
            self.connection.commit()
            print(f"✅ Data in '{table_name}' was successfully updated.")
        except sqlite3.Error as error:
            print(f"❌ Error when updating data: {error}")

    def get_book(self, table_name, condition):
        try:
            fetch_query = f"SELECT * FROM {table_name} WHERE {condition};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            print(f"✅ Data from '{table_name}' where '{condition}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Error when filtering data: {error}")

    def close_connection(self):
        self.connection.close()
        print("Connection Closed.")
