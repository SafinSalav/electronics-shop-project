from src.item import Item
import pytest


@pytest.fixture
def Item_():
    item = Item("Смартфон", 10000, 20)
    return item


def test_repr(Item_):
    assert repr(Item_) == "Item('Смартфон', 10000, 20)"


def test_str(Item_):
    assert str(Item_) == 'Смартфон'
