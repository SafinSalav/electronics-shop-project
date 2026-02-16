import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_phone(phone1):
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_add(item1, phone1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + item1 == 40


def test_set_zero_sim(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
