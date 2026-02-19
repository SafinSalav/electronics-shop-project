import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(keyboard1):
    assert keyboard1.name == 'Dark Project KD87A'
    assert keyboard1.price == 9600
    assert keyboard1.quantity == 5


def test_str(keyboard1):
    assert str(keyboard1) == "Dark Project KD87A"


def test_change_lang(keyboard1):
    assert str(keyboard1.language) == "EN"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "EN"
    with pytest.raises(AttributeError):
        keyboard1.language = 'CH'
