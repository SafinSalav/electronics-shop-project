import csv
from pathlib import Path
from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.

    :param pay_rate: Уровень цен с учетом скидки.
    :param all: Хранение созданных экземпляров класса.
    """
    pay_rate: float = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item и добавление его в all.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name: str = name
        self.price: float = price
        self.quantity: int = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        """
        Возвращает строку вида: "Item('iPhone 14', 120000, 5)".
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Возвращает название товара.
        """
        return self.__name

    def __add__(self, other) -> int:
        """
        Сложение экземпляров класса Phone и Item
        по количеству товара в магазине.
        """
        if isinstance(self, Item) and isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    @property
    def name(self) -> str:
        """
        Возвращает название товара.
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Позволяет переименовать название товара.
        """
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла .csv
        и заменяет ими старые экземпляры.
        """
        cls.all.clear()
        path = Path(__file__).resolve().parent.parent / file_path
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        if row['name'] and row['price'] and row['quantity']:
                            cls(
                                row['name'],
                                float(row['price']),
                                int(row['quantity'])
                            )
                        else:
                            raise InstantiateCSVError(
                                'Файл item.csv поврежден'
                            )
                except KeyError:
                    raise InstantiateCSVError(
                        'Файл item.csv поврежден'
                    ) from None
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv') from None

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
