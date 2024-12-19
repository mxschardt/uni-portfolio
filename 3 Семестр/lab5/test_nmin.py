import pytest

from nmin import nmin

tests = [([1, 2, 3, 4, 5], 4, 24),
         ([1, 0, 1, 2], 2, 0),
         ([-1, 10, 100, -3], 2, -300),
         ([5, 8, 1, 6, 4, 10, 1], 5, 120),
         ([8, 1, 1, 6, 0], 5, 0),
         ([-1, -2, -3, -4, 5], 4, 0),
         ([-5, -8, -1, 0], 2, 40),
         ([-1, -3, 4, 5], 2, -15),
         ([-100, 200, 1, 2, 3], 4, -600),
         ([], None),
         ([1, 2], None),
         ]


def test_simple_hypo():
    for test in tests:
        assert nmin(test[0], test[1]) == test[2]

def test_type_error():
    with pytest.raises(TypeError):
        nmin(['a', 'b'])

test_simple_hypo()