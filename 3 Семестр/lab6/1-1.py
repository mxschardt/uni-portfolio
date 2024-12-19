import random


class RandomNumberGenerator:
    def __init__(self, len, min, max):
        self.limit = len
        self.counter = 0
        self.min = min
        self.max = max

    def __next__(self):
        if self.limit <= self.counter:
            raise StopIteration

        self.counter += 1
        return random.randrange(self.min, self.max)

    def __iter__(self):
        return self


if __name__ == '__main__':
    rand = RandomNumberGenerator(5, 0, 10)
    print(rand)