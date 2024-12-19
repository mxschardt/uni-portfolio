"""
Для вычисления дисперсии и ср. квадр. отклонения использовать
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


class MathStats():

    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._combine = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        self._disp = None
        self._sigma_sq = None
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)
        for d in self._data:
            self._combine.append(d['Online'])
            self._combine.append(d['Offline'])

    @property
    def data(self):
        return self._data

    def visualize(self):
        monthly = self.monthly_sum(self._data)

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()

        for m in monthly:
            off = ax.barh(m["Month"],
                    m["Offline"],
                    left=0,
                    label="Online",
                    color="g")
            on = ax.barh(m["Month"],
                    m["Online"],
                    left=m["Offline"],
                    label="Offline",
                    color="c")
            ax.bar_label(off, label_type='center', color='k')
            ax.bar_label(on, label_type='center', color='k')

        for i, m in enumerate(monthly):
            total = m["Offline"] + m["Online"]
            ax.text(total+10, i+1.1, round(total),
                ha = 'center', weight = 'bold', color = 'black')

        plt.xlabel("Spend")
        plt.xticks()
        plt.ylabel("Month")
        plt.yticks(list(range(1, 13)))
        plt.title("Online and Offline Spending")

        ax.legend(["Online", "Offline"])
        plt.show()

    def sum_by_month(self, data, month):
        offline = 0
        online = 0
        for d in data:
            c = datetime.strptime(d["Date"], "%Y-%m-%d")
            if c.month == month:
                offline += d["Offline"]
                online += d["Online"]
        return (offline, online)

    def monthly_sum(self, data):
        months = []

        for i in range(1, 13):
            off, on = self.sum_by_month(data, i)
            months.append({"Month": i, "Offline": off, "Online": on})

        return months

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(data), sums['online'] / len(data))

        return self._mean

    @property
    def max(self):
        self._max = np.max(self._combine)
        return self._max

    @property
    def min(self):
        self._min = np.min(self._combine)
        return self._min

    @property
    def disp(self):
        # result = 0
        # mean = round(np.mean(self._combine), 2)
        # for d in self._combine:
        #     result += (d - mean)**2

        # return result / len(self._combine)
        self._disp = np.var(self._combine)
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        # return self.disp**(1 / 2)
        self._sigma_sq = np.std(self._combine)
        return self._sigma_sq
