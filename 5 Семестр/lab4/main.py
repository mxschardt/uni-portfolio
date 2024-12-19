# Задание 1
def fib(n):
    """
    Список чисел ряда Фибоначчи 

    Возвращает значения не превосходящие данное n

    Например: 
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]

    """
    if n < 0:
        return []
    if n == 0:
        return [0]
    a = 0
    b = 1
    result = [a, b]
    while a + b <= n:
        result.append(a + b)
        a = result[-2]
        b = result[-1]

    return result

# Задание 2
def is_fibonacchi(n):
    '''
    Натуральное число N является числом Фибоначчи тогда и только тогда, 
    когда 5N^2 + 4 или 5N^2 - 4 является квадратом. 
    Квадратное число — число, являющееся квадратом некоторого целого числа.
    '''
    from math import sqrt
    a = 5 * (n**2) - 4
    b = 5 * (n**2) + 4
    return a >= 0 and sqrt(a) % 1 == 0 \
     or b >= 0 and sqrt(b) % 1 == 0


class FibonacchiLst:

    def __init__(self, lst):
        self.lst = lst
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                current = self.lst[self.idx]
            except IndexError:
                raise StopIteration from IndexError

            self.idx += 1
            if is_fibonacchi(current):
                return current

# Задача 3
def fib_iter(lst):
    from itertools import filterfalse
    return filterfalse(lambda x: not is_fibonacchi(x), lst)


# Задание 4
def my_genn():
    a = 0
    b = 1
    while True:
        yield a
        res = a + b
        a = b
        b = res