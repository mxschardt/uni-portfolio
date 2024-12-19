class CurrenciesController:
    def __init__(self, model):
        self.model = model
        self.view = CurrenciesListView()

    def request_currencies(self):
        self.model.request_currencies()
        c = self.model.get_currencies()
        self.view(c)
    

class CurrenciesListView:
    def view(currencies):
        pass

    def __call__(self, currencies):
        for c in currencies:
            print(c, currencies[c])
