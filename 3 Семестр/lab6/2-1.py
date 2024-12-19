import time


def generate_fibonacci(limit):
    past, current = 0, 1
    for _ in range(limit):
        yield past
        past, current = current, current + past


class Timer:

    def __init__(self):
        self.start = time.perf_counter()

    def __enter__(self):
        return

    def __exit__(self, *args):
        end = time.perf_counter()
        print(end - self.start)


if __name__ == '__main__':
    with Timer():
        for _ in generate_fibonacci(1000000):
            pass
