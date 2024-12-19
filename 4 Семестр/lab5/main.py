import database as db

if __name__ == '__main__':
    connection = db.connect('db.sqlite')

    user_schema = [
        'id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT', 'height NUMBER',
        'created DATE'
    ]

    db.create_table(connection, 'user', user_schema)

    user = {'name': 'Petr', 'height': 1.6, 'created': '2023-03-04 12:15:20'}
    db.insert(connection, 'user', user)

    user = db.read(connection, 'user')
    print("Начальные значения")
    db.print_table(connection, 'user')

    print("Модифицированные значения")
    db.update(connection, 'user', "name = 'Nikita'", "name == 'Petr'")
    user = db.read(connection, 'user')
    db.print_table(connection, 'user')

    print("После удаления")
    db.delete(connection, 'user', "id > 5")
    db.print_table(connection, 'user')

    db.close(connection)
