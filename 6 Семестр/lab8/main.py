from currencies.currencies import CurrenciesDecoratorCSV, CurrenciesDecoratorJson, CurrenciesDict
from currencies.cbr_currencies_requester import CBRCurrenciesRequester

if __name__ == '__main__':
    requester = CBRCurrenciesRequester()
    c = CurrenciesDict(requester)

    c.request_currencies()
    cs = c.get_currencies()
    usd = c.get_currencies_by_id('R01235')

    c.set_tracked_currencies('R01335', 'R01239', 'R01235')
    tracked = c.get_tracked_currencies()

    c_csv = CurrenciesDecoratorCSV(c)
    csv_data = c_csv.get_tracked_currencies()

    c_json = CurrenciesDecoratorJson(c)
    json_data = c_json.get_tracked_currencies()
    # c.visualise()

    del c