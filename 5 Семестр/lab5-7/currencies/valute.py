from decimal import Decimal

class Valute:
    """
    Класс, представляющий валюту.

    Атрибуты:
        id (str): индвивидуальный индентификатор валюты.
        numCode (int): числовой код валюты.
        charcode (str): символьный код валюты.
        nominal (int): номинал валюты.
        name (str): название валюты.
        value (Decimal): значение валюты.
        vUnitRate (Decimal): курс единицы валюты.
    """

    def __init__(self, id: str, numCode: int, charcode: str, nominal: int,
                 name: str, value: str, vUnitRate: str):
        self.id = id
        self.numCode = numCode
        self.charcode = charcode
        self.nominal = nominal
        self.name = name
        self.value = Decimal(value)
        self.vUnitRate = Decimal(vUnitRate)

    def __str__(self) -> str:
        return f"{self.nominal} {self.name} ({self.charcode}): {self.value}"

    def __repr__(self) -> str:
        return f"Valute(id={self.id}, numCode={self.numCode:03}, charcode={self.charcode}, nominal={self.nominal}, name={self.name}, value={self.value}, vUnitRate={self.vUnitRate})"
