class InstantiateCSVError(Exception):
    """
    Класс исключения для поврежденного файла.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует исключение InstantiateCSVError.

        :param message: Сообщение об ошибке.
        """
        self.message = args[0] if args else 'CSV-файл поврежден.'

    def __str__(self):
        """
        Возвращает сообщение ошибки при ее срабатывании.
        """
        return self.message
