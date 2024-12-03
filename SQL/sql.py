import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor =  self.connection.cursor()
        print(f"Connection successfully to {db_name}")

    def create_table (self, table_name,columns):
        column_definitions = ""
        for name, dtype in columns.items():
            column_definitions += ", ".join([f"{name} {dtype}"])

        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        try:
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f" Table {table_name} successfuly created")
        except sqlite3.Error as e:
            print(f"The Error was found {e}")