# -*- coding: utf-8 -*-
#* Кодировка UTF-8: позволяет использовать текст на любом языке.
#? === Тема: Работа с базами данных (SQL) ===
# В этом уроке мы:
# 1. Подключимся к базе данных SQLite.
# 2. Выполним основные SQL-запросы (CREATE TABLE, INSERT, SELECT, UPDATE, DELETE).
# 3. Обработаем результаты запросов.
# 4. Добавим фильтры и условия для запросов.

import sqlite3  # SQLite — встроенная база данных в Python.

#* === Класс для работы с базой данных ===
class DatabaseManager:
    """
    Класс для управления подключением и взаимодействием с базой данных SQLite.
    """
    
    def __init__(self, db_name):
        """
        Конструктор: подключение к базе данных.
        :param db_name: Название файла базы данных (например, 'students.db').
        """
        try:
            #* Подключаемся к базе данных SQLite
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            print(f"✅ Подключение к базе данных '{db_name}' успешно установлено!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка подключения к базе данных: {error}")

    def create_table(self, table_name, columns):
        """
        Создаёт таблицу в базе данных.
        :param table_name: Название таблицы (str).
        :param columns: Словарь {имя_колонки: тип_данных}.
        """
        try:
            column_definitions = ""
            for name, dtype in columns.items():
                column_definitions += f"{name} {dtype}, "
            column_definitions = column_definitions.rstrip(", ") #! ОЧИЩАЕМ ОТ ЛИШНИХ ЗАПЯТЫХ И ПРОБЕЛОВ

            #* SQL-запрос для создания таблицы
            create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
            self.cursor.execute(create_query)
            self.connection.commit() #! БЕЗ ДАННОЙ КОММАНДЫ, ИЗМЕНЕНИЯ НЕ СОХРАНЯЮТСЯ В БД, А ОСТАНУТСЯ В ПАМЯТИ, ПОКА ПРОГРАММА РАБОТАЕТ (ПОСЛЕ ИЗМЕНЕНИЯ ПРОПАДАЮТ)

            print(f"✅ Таблица '{table_name}' успешно создана!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при создании таблицы: {error}")

    def insert_data(self, table_name, data):
        """
        Вставляет данные в таблицу.
        :param table_name: Название таблицы (str).
        :param data: Список кортежей, где каждый кортеж — одна строка данных.
        """
        try:
            #* Формируем запрос с placeholders (?) для подстановки значений.
            #! Количество колонок
            placeholders = ""
            for element in range(len(data[0])):
                placeholders += "?, "  
            """
            placeholders = "?, ?, ?, ?, "
            """
            placeholders = placeholders.rstrip(", ")
            #! Delete Trailing commas with space 
            """
            placeholders = "?, ?, ?, ?"
            """
            print('Вот как выглядит placeholders',placeholders)
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data)  #! Выполняем вставку данных.   
            """
                (NULL, "Alice", 20, 85.5),
                (NULL, "Bob", 22, 90.0),
                (NULL, "Charlie", 21, 78.3)
                (NULL, "Ken", 19, 75.5),
                (NULL, "Barbie", 17, 90.0),
            """
            self.connection.commit()
            print(f"✅ Данные успешно добавлены в таблицу '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при добавлении данных: {error}")

    def fetch_all(self, table_name):
        """
        Получает все данные из таблицы.
        :param table_name: Название таблицы (str).
        """
        try:
            fetch_query = f"SELECT * FROM {table_name};"
            self.cursor.execute(fetch_query)
            #? self.connection.commit()
            
            results = self.cursor.fetchall()
            print(f"✅ Получены данные из таблицы '{table_name}':")
            # print(f'VOT NASHI DANNIYE: {results}')
            for row in results:
                print(row)
            return results
        except sqlite3.Error as error:
            print(f"❌ Ошибка при получении данных: {error}")
            return []

    def fetch_by_condition(self, table_name, condition):
        """
        Получает данные из таблицы с условием.
        :param table_name: Название таблицы (str).
        :param condition: Условие SQL-запроса (например, "age > 20" НА ФОРМАТЕ SQL).
        """
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

    def update_data(self, table_name, updates, condition):
        """
        Обновляет данные в таблице.
        :param table_name: Название таблицы (str).
        :param updates: Строка обновлений (например, "grade = 95").
        :param condition: Условие SQL-запроса (например, "name = 'Alice'").
        """
        try:
            update_query = f"UPDATE {table_name} SET {updates} WHERE {condition};"
            self.cursor.execute(update_query)
            
            self.connection.commit() 

            print(f"✅ Данные в таблице '{table_name}' успешно обновлены!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при обновлении данных: {error}")

    def delete_data(self, table_name, condition):
        """
        Удаляет данные из таблицы.
        :param table_name: Название таблицы (str).
        :param condition: Условие SQL-запроса (например, "age < 20").
        """
        try:
            delete_query = f"DELETE FROM {table_name} WHERE {condition};"
            self.cursor.execute(delete_query)
            self.connection.commit()
            print(f"✅ Данные с условием '{condition}' успешно удалены из таблицы '{table_name}'!")
        except sqlite3.Error as error:
            print(f"❌ Ошибка при удалении данных: {error}")


    def change_column_name(self, table_name, old_column_name, new_column_name):
        """
        ALTER TABLE table_name RENAME COLUMN old_name to new_name;
        """

        change_query = f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} to {new_column_name}"
        self.cursor.execute(change_query)
        self.connection.commit()

        print(f'Column name changed from {old_column_name} to {new_column_name}')

    def close_connection(self):
        """
        Закрывает соединение с базой данных.
        """
        self.connection.close()
        print("✅ Соединение с базой данных закрыто.")

#* === Пример использования класса DatabaseManager ===
db = DatabaseManager("students.db")  # Подключаемся к базе данных.

# Создаём таблицу.
# db.create_table(
#     table_name="students_table",
#     columns={
#         "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
#         "name": "TEXT",
#         "age": "INTEGER",
#         "grade": "REAL",
#     }
# )

# # Вставляем данные.
# db.insert_data(
#     table_name="students_table",
#     data=[
#         (None, "BEKA", 22, 100),
#     ]
# )

# Получаем все данные.
# db.fetch_all("students_table")

# Фильтруем данные.
# db.fetch_by_condition(table_name="students_table", condition="age > 20")
# db.fetch_by_condition(table_name="students_table", condition="age > 20 and grade > 80")
# db.fetch_by_condition(table_name="students_table", condition="age > 20 or grade > 91")
# db.fetch_by_condition(table_name="students_table", condition="username=bekzat_dikhanov")
# db.fetch_by_condition(table_name="students_table", condition="bio=soft_dev")

# Обновляем данные.
# db.update_data("students_table", "grade = 89", "name = 'Charlie' and id=2")

# db.change_column_name(table_name="students_table", old_column_name='age', new_column_name='years_from_birth')
# db.change_column_name(table_name="students_table", old_column_name='years_from_birth', new_column_name='age')

# Удаляем данные.
db.delete_data("students_table", "id=7")

# # Закрываем соединение.
# db.close_connection()
