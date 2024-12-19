from main import fib, FibonacchiLst, fib_iter
import pytest


def test_fib():
    # n = 1
    assert fib(1) == [0, 1, 1]

    # n = 2
    assert fib(2) == [0, 1, 1, 2]

    # n = 5
    assert fib(5) == [0, 1, 1, 2, 3, 5]

    # n = 10
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]

    # n = 100
    assert fib(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # n = 0
    assert fib(0) == [0]

    # n = -1
    assert fib(-1) == []


def test_iteration():
    fib_lst = FibonacchiLst([])
    with pytest.raises(StopIteration):
        next(fib_lst)

    fib_lst = FibonacchiLst([4, 6, 7, 10])
    with pytest.raises(StopIteration):
        next(fib_lst)

    fib_lst = FibonacchiLst([0, 1, 1, 2, 3, 5, 8])
    assert list(fib_lst) == [0, 1, 1, 2, 3, 5, 8]

    fib_lst = FibonacchiLst([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert list(fib_lst) == [1, 2, 3, 5, 8]

    fib_lst = FibonacchiLst([-2, -1, 1, -3, 5, -8, -9])
    assert list(fib_lst) == [-2, -1, 1, -3, 5, -8]


def test_stop_iteration():
    fib_lst = FibonacchiLst([])
    with pytest.raises(StopIteration):
        next(fib_lst)

    fib_lst = FibonacchiLst([4, 6, 7, 10])
    with pytest.raises(StopIteration):
        next(fib_lst)

    fib_lst = FibonacchiLst([0, 1, 1, 2, 3, 5, 8])
    assert next(fib_lst) == 0
    assert next(fib_lst) == 1
    assert next(fib_lst) == 1
    assert next(fib_lst) == 2
    assert next(fib_lst) == 3
    assert next(fib_lst) == 5
    assert next(fib_lst) == 8
    with pytest.raises(StopIteration):
        next(fib_lst)

    fib_lst = FibonacchiLst([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert next(fib_lst) == 1
    assert next(fib_lst) == 2
    assert next(fib_lst) == 3
    assert next(fib_lst) == 5
    assert next(fib_lst) == 8
    with pytest.raises(StopIteration):
        next(fib_lst)


def test_fib_iter():
    fib_lst = []
    assert list(fib_iter(fib_lst)) == []

    fib_lst = [4, 6, 7, 10]
    assert list(fib_iter(fib_lst)) == []

    fib_lst = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    assert list(fib_iter(fib_lst)) == [0, 1, 1, 2, 3, 5, 8]

    fib_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(fib_iter(fib_lst)) == [1, 2, 3, 5, 8]

    fib_lst = [-2, -1, 1, -3, 5, -8, -9]
    assert list(fib_iter(fib_lst)) == [-2, -1, 1, -3, 5, -8]
