from threemin import threemin
import pytest

tests = [([1, 2, 3, 4, 5], 6),
         ([1, 0, 1, 2], 0),
         ([-1, 10, 100, -3], -3000),
         ([5, 8, 1, 6, 4, 10, 1], 4),
         ([8, 1, 1, 6, 0], 0),
         ([-1, -2, -3, -4], -24),
         ([-5, -8, -1, 0], -40),
         ([-1, -3, 4, 5], -60),
         ([-100, 1, 2, 3], -600),
         ([-100, 10, 3, 4], -4000),
         ([-1, 10, 20, 30], -600),
         ([], None),
         ([1, 2], None),
         ]


@pytest.mark.parametrize("inp_lst, expected", tests)
def test_simple_hypo(inp_lst, expected):
    assert threemin(inp_lst) == expected


def test_type_error():
    with pytest.raises(TypeError):
        threemin(['a', 'b'])
