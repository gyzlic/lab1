import doctest


class Table:
    def __init__(self, max_weight: float, current_weight: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param max_weight: Максимально допустимый вес на столе
        :param current_weight: Текущий вес предметов на столе

        Примеры:
        >>> table = Table(100.0, 0)  # инициализация экземпляра класса
        """
        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть типа int или float")
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным числом")
        self.max_weight = max_weight

        if not isinstance(current_weight, (int, float)):
            raise TypeError("Текущий вес должен быть int или float")
        if current_weight < 0:
            raise ValueError("Текущий вес не может быть отрицательным")
        self.current_weight = current_weight

    def is_empty_table(self) -> bool:
        """
        Проверяет, пуст ли стол

        :return: Является ли стол пустым

        Примеры:
        >>> table = Table(100.0, 0)
        >>> table.is_empty_table()
        """
        ...

    def add_item_to_table(self, item_weight: float) -> None:
        """
        Добавление предмета на стол.
        :param item_weight: Вес добавляемого предмета

        :raise ValueError: Если суммарный вес превышает максимально допустимый, вызывается ошибка

        Примеры:
        >>> table = Table(100.0, 0)
        >>> table.add_item_to_table(20.0)
        """
        if not isinstance(item_weight, (int, float)):
            raise TypeError("Вес предмета должен быть типа int или float")
        if item_weight < 0:
            raise ValueError("Вес предмета должен быть положительным числом")
        ...

    def remove_item_from_table(self, item_weight: float) -> None:
        """
        Удаление предмета со стола.

        :param item_weight: Вес удаляемого предмета
        :raise ValueError: Если вес удаляемого предмета больше текущего веса на столе, вызывается ошибка

        :return: Вес реально удаленного предмета

        Примеры:
        >>> table = Table(100.0, 50.0)
        >>> table.remove_item_from_table(20.0)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
