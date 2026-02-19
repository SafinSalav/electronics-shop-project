import pytest
from src.errors import InstantiateCSVError
from src.item import Item


def test_FileNotFoundError():
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.instantiate_from_csv('src/items.csv')


def test_InstantiateCSVError():
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv('src/items.csv')
