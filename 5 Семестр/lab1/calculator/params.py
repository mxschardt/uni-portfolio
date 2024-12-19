__all__ = ['calculate_file']

PARAMS = {'precision': 0.00001, 'dest': 'output.txt'}


def load_params(file="params.ini"):
    """ """
    global PARAMS
    f = open(file, mode='r', errors='ignore')
    lines = f.readlines()
    for l in lines:
        param = l.split('=')  # param[0], param[1]
        param[1] = param[1].strip('\n')

        if param[0] != 'dest':
            param[1] = eval(param[1])

        PARAMS[param[0]] = param[1]


def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    """
    Функция для записи в лог-файла

    Логика работы функции такая: 
    1. Пытаемся записать в файл данные.
    2. Если не получается, пытаемся это сделать в файл с новым именем.
    3. Если не получается и это, бросаем исключение Exception

    """
    error = None
    try:
        f = open(file, mode='a', errors='ignore')
        f.write(f"{action}: {args} = {result} \n")
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f"{action}: {args} = {result} \n")
        except PermissionError as e:
            error = e
            # print('Ошибка записи в файл')
            # print(f"{action}: {args} = {result}")
    finally:
        f.close()

    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')

def calculate_file(*args, **kwargs):
    """
    Основная функция для вычисления

    Реализуем следующую логику работы калькулятора: 
    1. Пытаемся загрузить настройки из файла. 
    2. Если не получается, загружаем настройки по умолчанию из переменной

    3. Выполняем действия по вычислению
    4. Выводим результаты вычисления на экран и 
    5. Пытаемся записать результаты вычисления в лог-файл. 
    6. Если не получается, выводим информацию о невозможности записи и данные, которые пытались записать в файл.

    Пункты списка 2 и 6 выполняются в модуле calculate на основе того, как отработали соответствующие функции  load_params и write_log.
    """

    load_params('params.ini')

    res = sum(args)

    try:
        write_log(*args, action='sum', result=res, file=PARAMS['dest'])
    except Exception as e:
        action = 'sum'
        print(e)
        print(f"{action}: {args} = {res}")