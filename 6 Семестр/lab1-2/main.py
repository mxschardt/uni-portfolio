from typing import List

import matplotlib.pyplot as plt

from mathstats import MathStats

RETAIL_PATH = "Retail.csv"
MARKETING_PATH = "MarketingSpend.csv"


def main():
    # запускающая функция
    data = read_data(RETAIL_PATH)

    c = count_invoice(data[:5])
    print(f"Всего инвойсов (invoices): {c}")  # 2
    c = count_invoice(data[:11])
    print(f"Всего инвойсов (invoices): {c}")  # 5
    c = count_invoice(data)
    print(f"Всего инвойсов (invoices): {c}")  # 16522

    data2 = MathStats(MARKETING_PATH)
    slice_test1 = data2.data[:2]  # первые две строки данных
    slice_test2 = data2.data[::]
    print(len(slice_test2))

    print(data2.get_mean(slice_test2))
    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)
    print(data2.max)
    print(data2.min)
    print(data2.disp)
    print(data2.sigma_sq)

    data2.visualize()
    # visualize_invoice1(data)


def visualize_invoice1(data):
    # data = {
    #     "InvoiceNo": _r["InvoiceNo"],
    #     "InvoiceDate": _r["InvoiceDate"],
    #     "StockCode": int(_r["StockCode"]),
    #     "Quantity": int(_r["Quantity"]),
    # }
    pass


def visualize_invoice(data):
    summary = {}
    stock_codes = set()
    for d in data:
        summary[d["InvoiceDate"]] = {}
    for d in data:
        summary[
            d["InvoiceDate"]][d["StockCode"]] = summary[d["InvoiceDate"]].get(
                d["StockCode"], 0) + d["Quantity"]
        stock_codes.add(d["StockCode"])

    dates = list(summary.keys())
    counts = set()
    stocks = {}
    for d in dates:
        for s in stock_codes:
            if not stocks.get(s):
                stocks[s] = []

            if summary[d].get(s):
                c = summary[d][s]
                counts.add(c)
                stocks[s].append(c)
            else:
                stocks[s].append(None)

    fig, ax = plt.subplots()

    for s in stock_codes:
        ax.scatter(dates, stocks[s], label=s)

    plt.xticks(range(1, 366), range(1, 366), rotation=-90)
    plt.yticks(list(counts))
    plt.legend()
    plt.show()

    return


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    import os

    data = []
    if not os.path.isfile(file):
        raise ValueError("File doesn't exist.")

    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for _r in reader:
            row = {
                "InvoiceNo": _r["InvoiceNo"],
                "InvoiceDate": _r["InvoiceDate"],
                "StockCode": int(_r["StockCode"]),
                "Quantity": int(_r["Quantity"]),
            }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.

    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # 3. Counter
    from collections import Counter

    # Реализуем получение номер invoices и помещение их в список
    # Переписать через генератор списка
    invoices = []
    for _el in data:
        invoices.append(_el["InvoiceNo"])

    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
    count = 0
    for d in data:
        if d[key]:
            count += 1
    return count


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданного товара для данного stock_code
    """

    result = 0
    for d in data:
        if d["StockCode"] == stock_code:
            result += d["Quantity"]
    return result


if __name__ == "__main__":
    main()
