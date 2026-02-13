"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture()
def Item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def Item2():
    return Item("Ноутбук", 20000, 5)


def test_Item_all(Item1, Item2):
    assert isinstance(Item.all, list)
    assert len(Item.all) == 2


def test_Item_calculate(Item1, Item2):
    assert Item1.calculate_total_price() == 200000
    assert Item2.calculate_total_price() == 100000


def test_Item_apply_discount(Item1, Item2):
    Item.pay_rate = 0.8
    Item1.apply_discount()
    assert Item1.price == 8000.0
    assert Item2.price == 20000
