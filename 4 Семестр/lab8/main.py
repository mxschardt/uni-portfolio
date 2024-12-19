from orator import DatabaseManager, Model, Schema

from database import Database
from model import User

config = {
    'default': 'sqlite',
    'sqlite': {
        'driver': 'sqlite',
        'database': 'db.sqlite'
    },
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)
schema = Schema(db)


def print_all_users():
    users = User.all()
    for user in users:
        print(f"{user.id}. {user.name} высотой {user.height} метров")
    print()


if __name__ == '__main__':

    # Создание таблицы, если она еще не создана
    if not schema.has_table('users'):
        with schema.create('users') as table:
            table.increments('id')
            table.string('name')
            table.float('height')

    print("Начальные данные:")
    print_all_users()

    # CREATE
    user = User()
    user.name = 'John'
    user.height = 1.8
    user.save()

    print("Добавление нового пользователя:")
    print_all_users()
    
    # READ
    user = User.find(1)
    print("Чтение пользователя с Id = 1:")
    print(user.name)

    # UPDATE
    user = User.find(1)
    user.height = 1.9
    user.save()
    print("Обновление высоты пользователя с Id = 1:")
    print_all_users()
    
    # DELETE
    user = User.find(1)
    user.delete()

    print("Удаление пользователя с Id = 1:")
    print_all_users()

    