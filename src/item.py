import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.

    :param pay_rate: Уровень цен с учетом скидки.
    :param all: Хранение созданных экземпляров класса.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item и добавление его в all.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self) -> str:
        """
        Возвращает __name.
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Позволяет переименовать __name.
        """
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла
        src/items.csv и заменяет ими старые экземпляры.
        """
        cls.all.clear()
        path = Path(__file__).resolve().parent.parent / file_path
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(number_string) -> int:
        """
        Возвращает число из числа-строки.
        """
        return int(float(number_string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
