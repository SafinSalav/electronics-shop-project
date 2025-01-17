from csv import DictReader


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(self, self.__class__):
            return self.quantity + other.quantity
        return None

    '''
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self._name = name
    '''

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def new_item(cls, *args):
        return cls(*args)

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all.clear()
        try:
            with open(path, encoding='utf-8', newline='') as csvfile:
                reader = DictReader(csvfile)
                for dic in reader:
                    Item.new_item(dic['name'], dic['price'], dic['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {path}')
        except KeyError:
            raise InstantiateCSVError(f'Файл {path} поврежден')


    @staticmethod
    def string_to_number(str):
        number = int(float(str))
        return number

