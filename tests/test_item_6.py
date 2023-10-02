from src.item import Item, InstantiateCSVError
import pytest


def test_1():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('item.csv')


def test_2():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/item.csv')

