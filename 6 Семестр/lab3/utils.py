import functools
import json
import os


class Memoize:

    def __init__(self):
        self.cache = {}

    def load_cache(self, path):
        if not os.path.isfile(path):
            return
        with open(path) as f:
            self.cache = dict(json.load(f))

    def dump_cache(self, path):
        with open(path, 'w') as f:
            json.dump(self.cache, f)

    def __call__(self, func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = str((func.__name__, args, str(kwargs)))
            if key not in self.cache:
                self.cache[key] = func(*args, **kwargs)
            return self.cache[key]

        return inner
