from unittest.mock import patch

import pytest

from currencies.cbr_currencies_requester import CBRCurrenciesRequester
from currencies.valute import Valute


@pytest.fixture
def mock_cbr_response():
    response_content = """
        <ValCurs Date="14.11.2023" name="Foreign Currency Market">
            <Valute ID="R01235">
                <NumCode>840</NumCode>
                <CharCode>USD</CharCode>
                <Nominal>1</Nominal>
                <Name>US Dollar</Name>
                <Value>72.50</Value>
                <VunitRate>1</VunitRate>
            </Valute>
            <Valute ID="R01239">
                <NumCode>978</NumCode>
                <CharCode>EUR</CharCode>
                <Nominal>1</Nominal>
                <Name>Euro</Name>
                <Value>85.10</Value>
                <VunitRate>1</VunitRate>
            </Valute>
        </ValCurs>
    """
    return response_content.encode()


def test_request_currencies(mock_cbr_response):
    requester = CBRCurrenciesRequester()

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = mock_cbr_response

        currencies = requester.request_currencies()

        assert requester.last_request is not None
        assert len(currencies) == 2
        assert isinstance(currencies[0], Valute)
        assert isinstance(currencies[1], Valute)
        assert currencies[0].charcode == "USD"
        assert currencies[1].charcode == "EUR"


def test_request_currencies_error(mock_cbr_response):
    requester = CBRCurrenciesRequester()

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 500
        mock_get.return_value.content = b"Server Error"

        with pytest.raises(Exception):
            requester.request_currencies()

        assert requester.last_request is None
        assert len(requester.valutes) == 0
