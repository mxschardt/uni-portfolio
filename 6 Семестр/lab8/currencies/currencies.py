from typing import Dict, List

from .base_currencies_requester import BaseCurrenciesRequester
from .valute import Valute, ValuteEncoder


class CurrenciesBase:
    """ """

    def request_currencies(self):
        """ """
        pass

    def get_currencies(self):
        """ """
        pass

    def get_currencies_by_id(self, *ids):
        """

        :param *ids:

        """
        pass

    def set_tracked_currencies(self, *ids):
        """

        :param *ids:

        """
        pass

    def get_tracked_currencies(self):
        """ """
        pass


class CurrenciesDict(CurrenciesBase):
    """Класс CurrenciesDict представляет собой хранилище и обработчик валют.


    """

    def __init__(self, requester: BaseCurrenciesRequester):
        self._requester = requester
        self._currencies = {}
        self._tracked_currencies = []

    def request_currencies(self) -> Dict[str, Valute]:
        """Запрашивает список валют у объекта requester и сохраняет его как словарь.


        :return: Словарь объектов `Valute`

        :rtype: dict[str, Valute]

        """
        currencies = self._requester.request_currencies()
        self._currencies.clear()
        for curr in currencies:
            self._currencies[curr.id] = curr

        return self._currencies

    def visualize(self) -> None:
        """Визуализирует отслеживымые валюты."""
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        currencies = []
        values = []
        for key, c in self._items():
            if key in self._tracked_currencies:
                append(str(c.name))
                values.append(c.vUnitRate)

        bars = ax.bar(currencies, values)
        ax.bar_label(bars)
        ax.set_ylabel("Значение валюты")
        ax.set_title("Курс валют")

        plt.show()

    def get_currencies(self) -> Dict[str, Valute]:
        """Возвращает:
        Cловарь со всеми валютами.


        """
        return self._currencies

    def get_currencies_by_id(self, *ids: str) -> Dict[str, Valute]:
        """Возвращает словарь, содержащий валюты с указанными id.
        При несуществующем id возвращает словарь вида {'R9999': None}.


        :return: Словарь, где ключи - id валюты, значения - объекты Valute или None.
        :rtype: Dict[str, Valute | None]

        :param *ids: id валют.
        :type *ids: str


        """
        res = {}
        for id in ids:
            res[id] = self._currencies.get(id)
        return res

    def set_tracked_currencies(self, *ids):
        """Устанавливает список отслеживаемых валют по заданным id.

        :param *ids: id валют.
        :type *ids: str


        """
        self._tracked_currencies = list(ids)

    def get_tracked_currencies(self) -> Dict[str, Valute]:
        """Возвращает словарь с отслеживаемыми валютами.

        :return: Словарь с отслеживаемыми валютами.
        :rtype: Dict[str, Valute | None]
        """
        return self.get_currencies_by_id(*self._tracked_currencies)

    def __del__(self):
        del self._currencies
        del self._tracked_currencies


class CurrenciesDecorator(CurrenciesBase):
    """ """

    def __init__(self, component: CurrenciesBase) -> None:
        self._component = component

    @property
    def component(self):
        """ """
        return self._component

    def request_currencies(self):
        """ """
        return self._component.request_currencies()

    def get_currencies(self):
        """ """
        return self._component.get_currencies()

    def get_currencies_by_id(self):
        """ """
        return self._component.get_currencies_by_id()

    def set_tracked_currencies(self, *ids):
        """

        :param *ids:

        """
        return self._component.set_tracked_currencies(ids)

    def get_tracked_currencies(self):
        """ """
        return self._component.get_tracked_currencies()


import json


class CurrenciesDecoratorJson(CurrenciesDecorator):
    """ """

    def request_currencies(self):
        """ """
        result = self._component.request_currencies()
        return json.dumps(result, cls=ValuteEncoder) if result else {}

    def get_currencies(self):
        """ """
        result = self._component.get_currencies()
        return json.dumps(result, cls=ValuteEncoder) if result else {}

    def get_currencies_by_id(self, *ids):
        """

        :param *ids:

        """
        result = self._component.get_currencies_by_id(*ids)
        return json.dumps(result, cls=ValuteEncoder) if result else {}

    def set_tracked_currencies(self, *ids):
        """

        :param *ids:

        """
        self._component.set_tracked_currencies(ids)

    def get_tracked_currencies(self):
        """ """
        result = self._component.get_tracked_currencies()
        return json.dumps(result, cls=ValuteEncoder) if result else {}


import io
import csv


class CurrenciesDecoratorCSV(CurrenciesDecorator):
    """ """

    def _dict_to_csv(self, d):
        """

        :param d:

        """
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        header = ["id", "numCode", "charcode", "nominal", "name", "value", "UnitRate"]
        writer.writerow(header)
        for _, v in d.items():
            row = [v.id, v.numCode, v.charcode, v.nominal, v.name, v.value, v.vUnitRate]
            writer.writerow(row)
        return output.getvalue()

    def request_currencies(self):
        """ """
        return self._dict_to_csv(self._component.request_currencies())

    def get_currencies(self):
        """ """
        return self._dict_to_csv(self._component.get_currencies())

    def get_currencies_by_id(self, *ids):
        """

        :param *ids:

        """
        return self._dict_to_csv(self._component.get_currencies_by_id(ids))

    def set_tracked_currencies(self, *ids):
        """

        :param *ids:

        """
        self._component.set_tracked_currencies(ids)

    def get_tracked_currencies(self):
        """ """
        return self._dict_to_csv(self._component.get_tracked_currencies())
