import random


def generate_random_numbers(limit, min, max):
    for _ in range(limit):
        yield random.randrange(min, max)


if __name__ == '__main__':
    numbers = generate_random_numbers(5, 0, 10)
    for n in numbers:
        print(n)
