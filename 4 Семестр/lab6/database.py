import sqlite3
from sqlite3 import Error
from typing import List

from singleton import singleton


@singleton
class Database():

    def __init__(self, connection_string):
        self._connection = self._connect(connection_string)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        self._connection.close()

    def connection(self):
        return self._connection

    def clear_table(self, table):
        cursor = self.connection().cursor()
        try:
            cursor.execute(f"DELETE FROM {table}")
        except Error as e:
            raise Exception('Очистка таблицы не удалась.') from e

    def read(self, table: str):
        cursor = self.connection().cursor()
        try:
            read_result = cursor.execute(f"SELECT * FROM {table}")
        except Error as e:
            raise Exception('Чтение из базы данных не удалось.') from e

        for _r in read_result:
            yield _r

    def create_table(self, table: str, schema) -> None:
        c = self.connection()
        cursor = c.cursor()
        try:
            insert_query = f"CREATE TABLE IF NOT EXISTS {table} ({','.join(schema)});"
            cursor.execute(insert_query)
            self.connection().commit()
        except Error as e:
            raise Exception(f'Ошибка при создании таблицы {table}.') from e

    def insert(self, table: str, values: dict[str, str]) -> None:
        if not self.connection():
            raise ValueError("Строка подключения не может быть пустой.")
    
        cursor = self.connection().cursor()
    
        try:
            placeholders = ', '.join([':' + key for key in values.keys()])
            columns = ', '.join(values.keys())
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, values)
    
            self.connection().commit()
    
        except Error as e:
            raise Exception(f"Ошибка при добавлении данных в таблицу {table}.") from e

    
    def insert_many(self, table: str, values: List[dict[str, str]]) -> None:
        if not self.connection():
            raise ValueError("Строка подключения не может быть пустой.")
        
        cursor = self.connection().cursor()
        
        try:
            columns = ', '.join(values[0].keys())
            placeholders = ', '.join([':' + key for key in values[0].keys()])
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.executemany(query, values)
        
            self.connection().commit()
        
        except Error as e:
            raise Exception(f"Ошибка при добавлении данных в таблицу {table}.") from e

    def delete(self, table: str, condition: str) -> None:
        cursor = self.connection().cursor()
        try:
            delete_query = f"DELETE FROM {table} WHERE {condition}"
            cursor.execute(delete_query)

            self.connection().commit()
        except Error as e:
            raise Exception(
                f"Ошибка при удалении данных из таблицы {table}") from e

    def _connect(self, connection_string):
        if not connection_string:
            raise ValueError("Строка подлючения не может быть пустой.")

        connection = None

        try:
            connection = sqlite3.connect(connection_string)
        except Error as e:
            raise Exception(
                f'Не удалось подключиться к БД {connection_string}.') from e

        return connection

    