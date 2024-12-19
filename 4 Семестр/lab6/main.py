from database import Database
from user import User

if __name__ == '__main__':
    # Создание схемы базы данных
    schema = [
        'id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT', 'height NUMBER',
        'created DATE'
    ]

    # Название таблицы
    table = 'user'
    
    # Создание пользователя через класс User и конвертация его в словарь для занесения полей в базу данных 
    user = User(
        'Ivan',
        1.9,
    ).dict()
    
    # Создание нескольких пользователей
    users = [User(chr(x), 1 + x / 10).dict() for x in range(65, 70)]
    
    # Открытие подключения к базе данных
    with Database('db.sqlite') as db:
        # Создание таблицы если ее нет
        db.create_table(table, schema)
        # Очистка таблицы
        # db.clear_table(table)

        print('Изначальные данные')
        for line in db.read('user'):
            print(line)
        print()

        # Добавление записей в БД
        db.insert(table, user) # Вставка только одного User
        db.insert_many(table, users) # Вставка нескольких User 
        
        print('Обновленные данные')
        for line in db.read('user'):
            print(line)
        print()

        # Удаление данных по условию
        db.delete(table, "name == 'Ivan'")
        print('После удаления')
        for line in db.read('user'):
            print(line)
