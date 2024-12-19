from datetime import datetime
from typing import List
from xml.etree import ElementTree

import requests

from currencies.base_currencies_requester import BaseCurrenciesRequester
from currencies.valute import Valute


class CBRCurrenciesRequester(BaseCurrenciesRequester):
    """
    Класс для запроса валют у Центрального банка Российской Федерации (ЦБР).

    Атрибуты:
        url (str): URL для запроса валют у ЦБР.
        last_request (datetime): Временная метка последнего запроса валют.
        valutes (list): Список значений валют.

    Методы:
        request_currencies(): Запрос и получение валют от ЦБР.
        _update_valutes_from_request(root): Обновление списка valutes на основе XML-ответа.
    """

    def __init__(self):
        self.url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        self.last_request = None
        self.valutes = []

    def request_currencies(self) -> List[Valute]:
        """
        Запрос и получение валют от ЦБР.

        Возвращает:
            List[Valute]: Список значений валют.

        Исключения:
            Exception: Если запрос к ЦБР завершился ошибкой.
        """
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Ошибка: " + str(response.status_code) + " " +
                            str(response.content))
        root = ElementTree.fromstring(response.content)
        self._update_valutes_from_request(root)
        self.last_request = datetime.now()
        return self.valutes

    def _update_valutes_from_request(self, root: ElementTree.Element):
        self.valutes.clear()
        for v in root.findall("Valute"):
            if (numCode := v.findtext('NumCode')) is None or \
                    (id := v.get('ID')) is None or \
                    (charcode := v.findtext('CharCode')) is None or \
                    (nominal := v.findtext('Nominal')) is None or \
                    (name := v.findtext('Name')) is None or \
                    (value := v.findtext('Value')) is None or \
                    (vUnitRate := v.findtext('VunitRate')) is None:
                raise Exception("Cound not get all Valute parametrs")

            numCode = int(numCode)
            nominal = int(nominal)
            value = value.replace(',', '.')
            vUnitRate = vUnitRate.replace(',', '.')

            self.valutes.append(
                Valute(id, numCode, charcode, nominal, name, value, vUnitRate))
