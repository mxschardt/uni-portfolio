from abc import ABC, abstractmethod
from typing import List

from currencies.valute import Valute


class BaseCurrenciesRequester(ABC):
    """
    Абстрактный базовый класс для запроса валют.

    Методы:
        request_currencies(): Запрос и получение валют.
    """

    @abstractmethod
    def request_currencies(self) -> List[Valute]:
        """
        Запрос и получение валют.

        Этот метод должен быть реализован в подклассах.
        """
        pass
