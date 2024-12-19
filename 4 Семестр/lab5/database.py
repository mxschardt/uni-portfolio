import sqlite3
from sqlite3 import Error
from typing import List, Tuple, Iterator, Dict


def connect(connection_string: str) -> sqlite3.Connection:
    if not connection_string:
        raise ValueError("Строка подлючения не может быть пустой.")

    try:
        db_connection = sqlite3.connect(connection_string)
    except Error as e:
        raise Exception(
            f'Не удалось подключиться к БД {connection_string}.') from e

    return db_connection


def close(connection: sqlite3.Connection) -> None:
    connection.close()


def read(connection: sqlite3.Connection, table: str) -> Iterator[Tuple]:
    if not connection:
        raise ValueError("Строка подлючения не может быть пустой.")

    cursor = connection.cursor()
    try:
        read_result = cursor.execute(f"SELECT * FROM {table}")
    except Error as e:
        raise Exception('Чтение из базы данных не удалось.') from e

    for _r in read_result:
        yield _r


def create_table(connection: sqlite3.Connection, table: str,
                 schema: List[str]) -> None:
    if not connection:
        raise ValueError("Строка подлючения не может быть пустой.")

    cursor = connection.cursor()
    try:
        insert_query = f"CREATE TABLE IF NOT EXISTS {table} ({','.join(schema)});"
        cursor.execute(insert_query)
        connection.commit()
    except Error as e:
        raise Exception(f'Ошибка при создании таблицы {table}.') from e


def insert(connection: sqlite3.Connection, table: str,
           user: Dict[str, str]) -> None:
    if not connection:
        raise ValueError("Строка подлючения не может быть пустой.")

    cursor = connection.cursor()
    try:
        tables = values = ""
        for i, (t, v) in enumerate(user.items()):
            tables += str(t)
            values += f"'{v}'"
            if i != len(user.items()) - 1:
                tables += ','
                values += ','

        insert_query = f"INSERT INTO {table} ({tables}) VALUES ({values});"
        cursor.execute(insert_query)
        connection.commit()
    except Error as e:
        raise Exception(
            f'Ошибка при добавлении данных в таблицу {table}.') from e


def update(connection: sqlite3.Connection, table: str, updated_ent: str,
           condition: str) -> None:
    if not connection:
        raise ValueError("Строка подлючения не может быть пустой.")

    cursor = connection.cursor()
    try:
        update_query = f"UPDATE {table} SET {updated_ent} WHERE {condition}"
        cursor.execute(update_query)

        connection.commit()
    except Error as e:
        raise Exception(
            f"Ошибка при обновлении данных в таблицу {table}") from e


def delete(connection: sqlite3.Connection, table: str, condition: str) -> None:
    if not connection:
        raise ValueError("Строка подлючения не может быть пустой.")

    cursor = connection.cursor()
    try:
        delete_query = f"DELETE FROM {table} WHERE {condition}"
        cursor.execute(delete_query)

        connection.commit()
    except Error as e:
        raise Exception(
            f"Ошибка при удалении данных из таблицы {table}") from e


def print_table(connection: sqlite3.Connection, table: str) -> None:
    for entry in read(connection, table):
        print(entry)
