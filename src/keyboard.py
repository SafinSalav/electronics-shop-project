from src.item import Item


class Mixin:
    i = 0

    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        self._language = ['RU', 'EN'][self.i % 2]
        Mixin.i += 1

    @property
    def language(self):
        return self._language


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
