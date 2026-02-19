from src.item import Item


class MixinLanguage:
    """
    Класс-миксин, который добавляет язык (раскладку клавиатуры).
    """
    def __init__(self):
        """
        Инициализация экземпляра класса MixinLanguage.

        :param language: Язык (раскладка клавиатуры).
        """
        self.__language = "EN"

    def change_lang(self) -> None:
        """
        Меняет язык (раскладку клавиатуры).
        """
        change = {
            "EN": "RU",
            "RU": "EN"
        }
        self.__language = change[self.__language]

    @property
    def language(self) -> str:
        """
        Возвращает язык (раскладку клавиатуры).
        """
        return self.__language


class Keyboard(Item, MixinLanguage):
    """
    Класс для представления клавиатуры, как товара в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
