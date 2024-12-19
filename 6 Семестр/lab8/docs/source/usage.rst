Usage
=====

Installation
------------

Для установки Currencies в своем проекте:

.. code-block:: console

   (.venv) $ git clone https://github.com/mxschardt/python-currencies


Получение списка валют
----------------------

Для получения списка валют необходимо создать класс, имплементирующий BaseCurrenciesRequester, а так же класс CurrenciesDict:

.. code-block:: python

    requester = CBRCurrenciesRequester()
    c = CurrenciesDict(requester)

    c.request_currencies()
    cs = c.get_currencies()
    usd = c.get_currencies_by_id('R01235')

    c.set_tracked_currencies('R01335', 'R01239', 'R01235')
    tracked = c.get_tracked_currencies()

BaseCurrenciesRequester
-----------------------

Абстрактный класс запросчика валют.

.. automodule:: currencies.base_currencies_requester

.. autoclass:: BaseCurrenciesRequester

CBRCurrenciesRequester
----------------------

Запросчик валют с сайта Центробанка.

.. automodule:: currencies.cbr_currencies_requester

.. autoclass:: CBRCurrenciesRequester

.. automethod:: CBRCurrenciesRequester.request_currencies

CurrenciesDict
--------------

Хранилище курсов валют.

.. automodule:: currencies.currencies

.. autoclass:: CurrenciesDict

.. automethod:: CurrenciesDict.request_currencies

.. automethod:: CurrenciesDict.get_currencies

.. automethod:: CurrenciesDict.get_currencies_by_id

.. automethod:: CurrenciesDict.set_tracked_currencies

.. automethod:: CurrenciesDict.get_tracked_currencies

.. automethod:: CurrenciesDict.visualize