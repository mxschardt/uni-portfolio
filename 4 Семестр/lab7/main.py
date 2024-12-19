import json


# Json может быть как массивом словарей так и отдельным словарем, так что
# возвращаем any
def load_json(filename) -> any:
    """
    Загрузка JSON-файла из диска.

    Args:
        filename (str): Имя файла для загрузки.

    Returns:
        any: Загруженные данные в формате JSON.

    Raises:
        Exception: Если файл не существует или имеет некорректные данные в формате JSON.
    """
    try:
        with open(filename, 'r') as f:
            result = json.load(f)
    except FileNotFoundError as e:
        # т.к. пустой файл тоже рассматривается как исключительная ситуация, то
        # смысла создавать пустой файл нет. создание корректного файла будет
        # отвественностью разработчика
        raise Exception(f"Файла '{filename}' не существует") from e
    except ValueError as e:
        raise Exception(f"Ошибка чтения файла ''{filename}'' в json") from e

    return result


def save_json(filename, file):
    """
    Сохранение данных в JSON-файл.

    Args:
        filename (str): Имя файла для сохранения.
        file (any): Данные для сохранения в файле.

    Returns:
        None

    Raises:
        Exception: Если возникла ошибка записи в файл.
    """
    try:
        with open(filename, 'w') as f:
            f.write(json.dumps(file))
    except ValueError as e:
        raise Exception(f"Ошибка чтения файла '{filename}'") from e


def print_json(file):
    """
    Вывод данных в формате JSON на консоль .

    Args:
        file (any): Данные в формате JSON для вывода.

    Returns:
        None
    """
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(file)

def validate_json(file, validation) -> bool:
    """
    Проверка данных в формате JSON на соответствие структуре.

    Args:
        file (any): Данные в формате JSON для проверки.
        validation (dict): Словарь, указывающий ожидаемые ключи и типы данных для структуры JSON.

    Returns:
        bool: True, если данные в формате JSON соответствуют структуре, False в противном случае.
    """
    # Если файла не существует или файл пустой
    if not file or len(file) == 0:
        return False

    # Если файл типа массив
    if type(file) == type([]):
        # Для каждого объекта в массиве проводим отдельную проверку
        for field in file:
            # Если проверка не прошла, возвращаем False.
            if not _validate_json_dict(field, validation):
                return False
    # Если файл типа словарь
    elif type(file) == type({}):
        # Нужна только одна проверка. Если она не прошла,
        # возвращаем False.
        if not _validate_json_dict(file, validation):
            return False
    # Другие типы данных считаются невалидными
    else:
        return False

    # Файл прошел все проверки и является валидным Json файлом
    return True


def _validate_json_dict(file, validation) -> bool:
    # Проверка ключей
    if file.keys() != validation.keys():
        raise KeyError(f"Поля файла '{file}' не совпадают с ключами валидации")

    # Проверка типов ключей
    for key, val in validation.items():
        if val != type(file[key]):
            raise TypeError(
                f"Тип поля '{key}' '{type(file[key])}' не соврадает с типом поля валидации '{val}'"
            )

    # Проверка прошла успешно
    return True


def add_users(users, validation) -> list:
    """
    Добавление данных о пользователях с клавиатуры.

    Args:
        users (list or dict): Существующие данные о пользователях для добавления.
        validation (dict): Словарь, указывающий ожидаемые ключи и типы данных для структуры данных о пользователях.

    Returns:
        list: Обновленные данные о пользователях.

    """
    while (input('Ввести нового пользователя? y/N\n') == 'y'):
        new_user = _read_user(validation)

        # Добавление нового объекта к существующим
        if type([]) == type(users):
            users.append(new_user)
        else:
            users = [users, new_user]
    
    return users


# Вводим поля из validation и приводим их к корректному типу
def _read_user(validation) -> any:
    import ast

    result = {}
    for key, val in validation.items():
        while True:
            input_value = input(f"Введите значение для ключа '{key}': ")
            if not input_value:
                print("Значение не может быть пустым")
                continue
            if val == str:
                casted_value = input_value
                break

            try:
                casted_value = ast.literal_eval(input_value)
                if type(casted_value) != val:
                    raise ValueError()
            except (ValueError, SyntaxError):
                print("Не удалось установить корректный тип данных")
            else:
                break

        result[key] = casted_value

    return result


if __name__ == '__main__':


    # Объект для валидации Json { 'название поля': тип поля }
    validation = {
        "name": str,
        "gender": str,
        "email": str,
        "phone": str,
        "address": str,
        "friends": list
    }

    try:
        # Загрузка Json из файла
        users = load_json('data.json')

        # Валидация объекта
        validate_json(users, validation)

        # Исходный файл
        print_json(users)

        # Создание новый пользователей
        new_users = add_users(users, validation)

        # Модифицированный файл
        print_json(new_users)

        # Сохранение нового файла
        save_json('clients_data.json', new_users)
    except Exception as e:
        raise e

