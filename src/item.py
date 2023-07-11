
import csv
import os

#items_csv = os.path.join("src", "items.csv") # путь к файлу при тестировании
items_csv = os.path.join("..", "src", "items.csv") # путь к файлу при работе программы
#items_csv = r'D:\PycharmProjects\pythonProject\electronics-shop-project\src\items.csv'


class InstantiateCSVError(Exception):
    """
    Класс-исключение `InstantiateCSVError`
    """

    def __init__(self, *args, **kwargs):
        self.message = "Файл item.csv поврежден"


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"


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
        self.price *= self.pay_rate


    @property
    def name(self):
        """
        Выводит имя объекта класса Item
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Присваивает новое имя объекту класса Item, длинной не более 10 символов
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name


    @staticmethod
    def checking_file_items():
        """
        Выполняет проверку файла "items.csv"
        """
        with open(items_csv, encoding="windows-1251") as csvfile:
            file = csv.reader(csvfile)
            headers = next(file)
            if not (headers[0] == "name" and headers[1] == "price" and headers[2]) == "quantity":
                raise InstantiateCSVError


    @classmethod
    def instantiate_from_csv(cls):
        """
        Создает объекты класса Item на основе файла "items.csv"
        - если файл `items.csv`, из которого по умолчанию считываются данные, не найден →
        выбрасывается исключение `FileNotFoundError` с сообщением “_Отсутствует файл item.csv_"
        - если файл `item.csv` поврежден (например, отсутствует одна из колонок данных) →
        выбрасывается исключение `InstantiateCSVError` с сообщением “_Файл item.csv поврежден_”
        """
        try:
            cls.checking_file_items()
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError as ex:
            print(ex.message)
        else:
            with open(items_csv, encoding="windows-1251") as csvfile:
                file = csv.DictReader(csvfile)
                for line in file:
                    name, price, quantity = line["name"], float(line["price"]), cls.string_to_number(line["quantity"])
                    cls(name, price, quantity)


    @staticmethod
    def string_to_number(string):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))


    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
