from decimal import Decimal

from currencies.valute import Valute


def test_valute_init():
    """ """
    valute = Valute("R01010", 36, "AUD", 1, "Австралийский доллар", "58.5874",
                    "58.5874")

    assert valute.id == "R01010"
    assert valute.numCode == 36
    assert valute.charcode == "AUD"
    assert valute.nominal == 1
    assert valute.name == "Австралийский доллар"
    assert valute.value == Decimal("58.5874")
    assert valute.vUnitRate == Decimal("58.5874")
