from currencies.cbr_currencies_requester import CBRCurrenciesRequester
from currencies.currencies import Currencies
from currencies.currencies_controller import CurrenciesController

if __name__ == '__main__':
    requester = CBRCurrenciesRequester()

    model = Currencies(requester)

    controller = CurrenciesController(model)

    controller.request_currencies()



    # c.request_currencies()
    # cs = c.get_currencies()
    # usd = c.get_currencies_by_id('R01235')
    # print(usd)
    # c.set_tracked_currencies('R01335', 'R01239')
    # tracked = c.get_tracked_currencies()
    # print(tracked)
    # del cs
    # res = get_currencies(['R01035', 'R01335', 'R01700J'])
    # if res:
    #     print(get_currencies(['R01035', 'R01335', 'R01700J']))
