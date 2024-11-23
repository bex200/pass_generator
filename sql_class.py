# -*- coding: utf-8 -*-
#* Кодировка UTF-8: позволяет использовать текст на любом языке.
#? === Тема: Работа с базами данных (SQL) ===
# В этом уроке мы:
# 1. Подключимся к базе данных SQLite.
# 2. Выполним SQL-запросы (CREATE TABLE, INSERT, SELECT).
# 3. Обработаем результаты запросов.

import sqlite3  # SQLite - встроенная база данных в Python. 

#* === Класс для работы с базой данных ===
class DatabaseManager:
    """
    Класс для управления подключением и взаимодействием с базой данных SQLite.
    """
    def __init__(self, db_name):
        """
        Конструктор: инициализация подключения к базе данных.
        :param db_name: Название файла базы данных (например, 'students.db').
        """
        #* Подключаемся к базе данных
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"✅ Подключение к базе данных '{db_name}' успешно установлено!")

    def create_table(self, table_name, columns):
        """
        Создаёт таблицу с заданными столбцами.
        :param table_name: Название таблицы.
        :param columns: Словарь вида {имя колонны: тип данных, имя колонны: тип данных, имя колонны: тип данных}.
        """
        #* Формируем SQL-запрос для создания таблицы
        # column_definitions = ", ".join([f"{name} {dtype}" for name, dtype in columns.items()])
        column_definitions = ''
        for name, dtype in columns.items():
            column_definitions += ", ".join([f'{name} {dtype}'])
            #! ', '.join(['user_emails UserEmails'])

        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        
        try:
            self.cursor.execute(create_query)
            self.connection.commit()
            print(f"✅ Таблица '{table_name}' успешно создана!")
        except sqlite3.Error as e:
            print(f"❌ Ошибка при создании таблицы: {e}")

    def insert_data(self, table_name, data):
        """
        Вставляет данные в таблицу.
        :param table_name: Название таблицы.
        :param data: Список кортежей с данными для вставки.
        """
        try:
            #* Формируем SQL-запрос для вставки данных
            placeholders = ", ".join(["?" for _ in data[0]])
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
            self.cursor.executemany(insert_query, data)
            self.connection.commit()
            print(f"✅ Данные успешно добавлены в таблицу '{table_name}'!")
        except sqlite3.Error as e:
            print(f"❌ Ошибка при добавлении данных: {e}")

    def fetch_data(self, table_name):
        """
        Получает все данные из таблицы.
        :param table_name: Название таблицы.
        :return: Список кортежей с данными.
        """
        try:
            #* Формируем SQL-запрос для получения данных
            select_query = f"SELECT * FROM {table_name};"
            self.cursor.execute(select_query)
            results = self.cursor.fetchall()
            print(f"✅ Получены данные из таблицы '{table_name}':")
            for row in results:
                print(row)
            return results
        except sqlite3.Error as e:
            print(f"❌ Ошибка при получении данных: {e}")
            return []

    def close_connection(self):
        """
        Закрывает соединение с базой данных.
        """
        self.connection.close()
        print("✅ Соединение с базой данных закрыто.")


#* === Пример использования класса DatabaseManager ===
if __name__ == "__main__":
    #? 1. Создаём экземпляр класса и подключаемся к базе данных
    db = DatabaseManager("students.db")  # Создаётся файл базы данных students.db.

    #? 2. Создаём таблицу 'students'
    db.create_table(
        "students",
        {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Уникальный ID
            "name": "TEXT",  # Имя студента
            "age": "INTEGER",  # Возраст студента
            "grade": "REAL"  # Оценка студента
        }
    )

    # #? 3. Вставляем данные в таблицу
    db.insert_data(
        "students",
        [
            (None, "Alice", 20, 85.5),  # None для автозаполнения ID
            (None, "Bob", 22, 90.0),
            (None, "Charlie", 21, 78.3)
        ]
    )

    #? 4. Получаем и выводим данные из таблицы
    db.fetch_data("students")

    #? 5. Закрываем соединение
    db.close_connection()








