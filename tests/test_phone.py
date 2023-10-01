from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_phone(phone):
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2


def test(phone, item):
    assert item + phone == 25
    assert phone + phone == 10


def test_change_number_of_sim(phone):
    number_sim = phone.number_of_sim
    phone.number_of_sim = 0
    assert phone.number_of_sim == number_sim
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
