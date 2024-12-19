import random


def generate_fibonacci(limit):
    past, current = 0, 1
    for _ in range(limit):
        yield past
        past, current = current, current + past


def add_10(numbers):
    for n in numbers:
        yield n + 10


if __name__ == '__main__':
    numbers = add_10(generate_fibonacci(10))
    for n in numbers:
        print(n)
