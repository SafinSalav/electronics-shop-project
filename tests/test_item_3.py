import pytest
from src.item import Item


@pytest.fixture
def Item1():
    return Item("Смартфон", 10000, 20)


def test_repr(Item1):
    assert repr(Item1) == "Item('Смартфон', 10000, 20)"


def test_str(Item1):
    assert str(Item1) == 'Смартфон'
