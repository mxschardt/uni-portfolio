from decimal import Decimal

import pytest

from currencies.base_currencies_requester import BaseCurrenciesRequester
from currencies.currencies import Currencies


class MockCurrenciesRequester(BaseCurrenciesRequester):
    """ """

    def request_currencies(self):
        """ """
        return [
            Valute('RUB', 643, 'RUB', 1, 'Russian Ruble', '1', '1'),
            Valute('USD', 840, 'USD', 1, 'US Dollar', '1', '1'),
            Valute('EUR', 978, 'EUR', 1, 'Euro', '1', '1'),
        ]


@pytest.fixture
def currencies():
    """ """
    return Currencies(MockCurrenciesRequester())


class Valute:
    """ """

    def __init__(self, id, numCode, charcode, nominal, name, value, vUnitRate):
        self.id = id
        self.numCode = numCode
        self.charcode = charcode
        self.nominal = nominal
        self.name = name
        self.value = Decimal(value)
        self.vUnitRate = Decimal(vUnitRate)


def test_request_currencies(currencies):
    """

    :param currencies: 

    """
    currencies.request_currencies()
    assert len(currencies.get_currencies()) == 3


def test_get_currencies(currencies):
    """

    :param currencies: 

    """
    currencies.request_currencies()
    all_currencies = currencies.get_currencies()
    assert len(all_currencies) == 3
    assert all(
        isinstance(valute, Valute) for valute in all_currencies.values())


def test_get_currencies_by_id(currencies):
    """

    :param currencies: 

    """
    currencies.request_currencies()
    currency = currencies.get_currencies_by_id('RUB')
    assert isinstance(currency, dict)
    assert 'RUB' in currency
    assert isinstance(currency['RUB'], Valute)

    nonexistent_currency = currencies.get_currencies_by_id('XYZ')
    assert 'XYZ' in nonexistent_currency
    assert nonexistent_currency['XYZ'] is None


def test_set_tracked_currencies(currencies):
    """

    :param currencies: 

    """
    currencies.set_tracked_currencies('USD', 'EUR')
    tracked_currencies = currencies.get_tracked_currencies()
    assert len(tracked_currencies) == 2
    assert 'USD' in tracked_currencies
    assert 'EUR' in tracked_currencies


def test_get_tracked_currencies(currencies):
    """

    :param currencies: 

    """
    currencies.request_currencies()
    currencies.set_tracked_currencies('USD', 'EUR')
    tracked_currencies = currencies.get_tracked_currencies()
    assert len(tracked_currencies) == 2
    assert 'USD' in tracked_currencies
    assert 'EUR' in tracked_currencies
    assert isinstance(tracked_currencies['USD'], Valute)
    assert isinstance(tracked_currencies['EUR'], Valute)
