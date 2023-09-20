from src.item import Item
import pytest


@pytest.fixture
def Item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture
def Item2():
    item2 = Item("Ноутбук", 20000, 5)
    return item2


def test_calculate_total_price(Item1, Item2):
    assert Item1.calculate_total_price() == 200000
    assert Item2.calculate_total_price() == 100000


def test_discount(Item1, Item2):
    Item.pay_rate = 0.8
    Item1.apply_discount()
    assert Item1.price == 8000.0
    assert Item2.price == 20000
