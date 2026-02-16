from src.item import Item
import pytest


@pytest.fixture()
def Item1():
    return Item("Телефон", 10000, 5)


@pytest.fixture()
def Items():
    Item.instantiate_from_csv('src/items.csv')
    return Item.all


def test_name(Item1):
    assert Item1.name == "Телефон"
    Item1.name = 'Смартфон'
    assert Item1.name == 'Смартфон'
    Item1.name = 'СуперСмартфон'
    assert Item1.name == 'СуперСмарт'


def test_instantiate_from_csv(Items):
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
