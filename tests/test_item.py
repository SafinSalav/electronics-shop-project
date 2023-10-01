from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def Item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture
def Item2():
    item2 = Item("Ноутбук", 20000, 5)
    return item2


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(Item1, Item2):
    assert Item1.calculate_total_price() == 200000
    assert Item2.calculate_total_price() == 100000


def test_discount(Item1, Item2):
    Item.pay_rate = 0.8
    Item1.apply_discount()
    assert Item1.price == 8000.0
    assert Item2.price == 20000


def test_phone(phone):
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2


def test_add(phone, Item1):
    assert Item1 + phone == 25
    assert phone + phone == 10


def test_change_number_of_sim(phone):
    number_sim = phone.number_of_sim
    phone.number_of_sim = 0
    assert phone.number_of_sim == number_sim
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
