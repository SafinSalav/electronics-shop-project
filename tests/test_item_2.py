from src.item import Item
import pytest


@pytest.fixture
def Item_():
    item = Item("Телефон", 10000, 5)
    return item


@pytest.fixture
def Items():
    Item.instantiate_from_csv('../src/items.csv')
    return Item.all


def test_name(Item_):
    Item_.name = 'Смартфон'
    assert Item_.name == 'Смартфон'


def test_name_2(Item_):
    Item_.name = 'СуперСмартфон'
    assert Item_.name == 'СуперСмартфон'[:10]


def test_count_items(Items):
    assert len(Items) == 5


def test_item1(Items):
    item1 = Items[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
