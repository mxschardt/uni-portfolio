from flask import Flask

from utils import Memoize

app = Flask(__name__)
memoized = Memoize()


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/about')
def about():
    return 'Maxim Schardt'


@app.route('/calc/<string:func>/<int:n>')
# @functools.cache
@memoized
def factorial(func: str, n: int):
    from math import factorial as f1

    from scipy.special import factorial as f2

    if func == "f1":
        return str(f1(n))
    elif func == "f2":
        return str(int(f2(n)))

    return ""


if __name__ == '__main__':
    cache_path = "cache.json"
    # Load cache
    memoized.load_cache(cache_path)

    app.run(host='0.0.0.0', port=80)

    # Store cache
    memoized.dump_cache(cache_path)
