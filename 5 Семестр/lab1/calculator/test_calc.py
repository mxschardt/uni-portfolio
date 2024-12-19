__all__ = ['test_calc_simple']

from .calc import calculate


def test_calc_simple():
  assert calculate(1, 1, '+') == 2


def test_calc_sub():
  assert calculate(1, 1, '-') == 0


def test_calc_multiply():
  assert calculate(2, 2, '*') == 4


def test_calc_div_1():
  assert calculate(1, 0, '/') is None


def test_calc_div_2():
  assert calculate(1, 2, '/') == 0.5

def test_calc_and():
  assert calculate(1250, 100, 'AND') == 96

def test_calc_or():
  assert calculate(2540, 4100, 'OR') == 6636
