import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            print(f"✅ Подключение к базе данных '{db_name}' успешно установлено!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка подключения к базе данных: {error}")

    def create_table(self, table_name, columns):
        try:
            column_definitions = ""
            for name, dtype in columns.items():
                column_definitions += f"{name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ")
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"✅ Таблица '{table_name}' успешно создана!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при создании таблицы: {error}")


    def insert_data(self, table_name, data):
        try:
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "
            placeholders = placeholders.rstrip(", ")
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data)
            self.connection.commit()
            print(f"✅ Данные успешно добавлены в таблицу '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при добавлении данных: {error}")

    def fetch_by_condition(self, table_name, condition):
        try:
            fetch_query = f"SELECT * FROM {table_name} WHERE {condition};"
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            print(f"✅ Данные из таблицы '{table_name}' с условием '{condition}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Ошибка при фильтрации данных: {error}")
            return []

    def fetch_all(self, table_name):
        try:
            fetch_query = f"SELECT * FROM {table_name};"
            self.cursor.execute(fetch_query)

            results = self.cursor.fetchall()
            print(f"✅ Получены данные из таблицы '{table_name}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Ошибка при получении данных: {error}")
            return []


    def update_data(self, table_name, updates, condition):
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            self.cursor.execute(update_query)
            self.connection.commit()
            print(f"✅ Данные в таблице '{table_name}' успешно обновлены!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при обновлении данных: {error}")


    def delete_data(self, table_name, condition):
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"✅ Данные с условием '{condition}' успешно удалены из таблицы '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при удалении данных: {error}")


    def close_connection(self):
        self.connection.close()
        print("✅ Соединение с базой данных закрыто.")