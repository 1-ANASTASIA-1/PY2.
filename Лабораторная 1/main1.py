from typing import Union
import doctest

# Второй класс
class Table:
    def __init__(self, height: Union[int, float], square: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Стол"
        :param height: Выстоа стола в см
        :param square: Ширина стола в см
        Примеры:
        >>> table = Table(80, 9600)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должена быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стола должена быть положительным числом")
        self.height = height

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь стола должена быть типа int или float")
        if square <= 0:
            raise ValueError("Площадь стола должена быть положительным числом")
        self.square = square

    def is_children_table(self) -> bool:
        """
        Функция которая проверяет является ли стол детским
        :return: Является ли стол детским
        Примеры:
        >>> table = Table(80, 9600).is_children_table()
        """
        ...

    def reduce_square_to_table(self, reduce_square: float) -> None:
        """
        Уменьшения площади стола.
        :param reduce_square: Площадь уменьшаемой площади
        :raise ValueError: Если уменьшаемая площадь стола превышает площадь стола, то вызываем ошибку
        Примеры:
        >>> table = Table(80, 9600)
        >>> table.reduce_square_to_table(200)
        """
        if not isinstance(reduce_square, (int, float)):
            raise TypeError("Уменьшаемая площадь должна быть типа int или float")
        if reduce_square < 0:
            raise ValueError("Уменьшаемая площадь должна положительным числом")
        ...

    def add_square_to_table(self, add_square) -> None:
        """
        Увеличение площади стола.
        :param add_square: Площадь увеличиваемой площади
        Примеры:
        >>> table = Table(80, 9600)
        >>> table.add_square_to_table(200)
        """
        if not isinstance(add_square, (int, float)):
            raise TypeError("Увеличиваемая площадь должна быть типа int или float")
        if add_square < 0:
            raise ValueError("Увеличиваемая площадь должна быть отрицательным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
