import numpy

__settings = {"precision": "0.00000001"}


def main():
  """
  Основная запускающая функция. 
  Задачи: 
  - Принять от пользователя операнды,
  - Запустить на вычисление функцию calculate,
  - Вывести значение результата на экран.
  """
  try:
    operands = list(
      map(lambda x: float(x),
          input("Введите опреанды через пробел: ").strip().split(" ")))

    action = input("Введите действие: ")

    result = calculate_multiple(operands, action)

    print(f"Равно: {result}")
  except:
    print("Что-то пошло не так...")


def calculate_multiple(operands: list, action: str) -> int:
  if len(operands) == 0 or not all(isinstance(n, float) for n in operands):
    return None
  result = operands.pop()
  while len(operands) != 0:
    result = calculate(result, operands.pop(), action)

  return result


def calculate(a: int, b: int, action, settings=__settings) -> int:
  result = None
  if action == "+":
    result = a + b
  elif action == "-":
    result = a - b
  elif action == "*":
    result = a * b
  elif action == "/":
    try:
      result = a / b
    except ZeroDivisionError:
      return None
  elif action == "**":
    result = a**b
  elif action == "&":
    result = a & b
  elif action == "|":
    result = a | b

  return round(result, convert_precision(settings.get("precision")))


def convert_precision(precision) -> int:
  for i in range(len(str(precision))):
    if float(precision) * 10**i >= 1:
      return i


def std_dev(*args, precision="0.000001") -> float:
  return round(numpy.std(numpy.array(args)), convert_precision(precision))


if __name__ == "__main__":
  main()
