from src.item import Item


class Phone(Item):
    """
    Класс для представления смартфона, как товара в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых SIM-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """
        Возвращает количество SIM-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim) -> None:
        """
        Позволяет поменять количество SIM-карт.
        """
        if new_number_of_sim > 0:
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно "
                             "быть целым числом больше нуля.")

    def __repr__(self) -> str:
        """
        Возвращает строку вида: "Phone('iPhone 14', 120000, 5, 2)".
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
