from currencies.base_currencies_requester import BaseCurrenciesRequester


class Currencies:
    """
    Класс Currencies представляет собой хранилище и обработчик валют.
    
    Методы:
        request_currencies(): Запрашивает список валют у requester и сохраняет его.
        get_currencies(): Возвращает список всех валют.
        get_currencies_by_id(*ids): Возвращает словарь, содержащий валюты с указанными id.
        set_tracked_currencies(*ids): Устанавливает список отслеживаемых валют по заданным id.
        get_tracked_currencies(): Возвращает словарь с отслеживаемыми валютами.
    """

    def __init__(self, requester: BaseCurrenciesRequester):
        self._requester = requester
        self._currencies = {}
        self._tracked_currencies = []

    def request_currencies(self):
        """
        Запрашивает список валют у объекта requester и сохраняет его как словарь.
        """
        currencies = self._requester.request_currencies()
        self._currencies.clear()
        for curr in currencies:
            self._currencies[curr.id] = curr

    def get_currencies(self):
        """
        Возвращает словарь со всеми валютами.
        """
        return self._currencies

    def get_currencies_by_id(self, *ids):
        """
        Возвращает словарь, содержащий валюты с указанными id. 
        При несуществующем id возвращает словарь вида {'R9999': None}.
        
        Аргументы:
            *ids: id валют.
        
        Возвращает:
            dict: Словарь, где ключи - id валюты, значения - объекты Valute или None.
        """
        res = {}
        for id in ids:
            res[id] = self._currencies.get(id)
        return res

    def set_tracked_currencies(self, *ids):
        """
        Устанавливает список отслеживаемых валют по заданным id.
        
        Аргументы:
            *ids: Переменное количество id валют.
        """
        self._tracked_currencies = list(ids)

    def get_tracked_currencies(self):
        """
        Возвращает словарь с отслеживаемыми валютами.
        """
        return self.get_currencies_by_id(*self._tracked_currencies)

    def __del__(self):
        del self._currencies
        del self._tracked_currencies