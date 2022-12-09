from typing import Union
import doctest

# Третий класс
class Washer:
    def __init__(self, value: Union[int, float], occupied_value: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Стол"
        :param value: Объем барабана стиральной машины
        :param occupied_value: Объем занимаемый вещами
        Примеры:
        >>> washer = Washer(30, 10)  # инициализация экземпляра класса
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Оъем стиральной машины должен быть типа int или float")
        if value <= 0:
            raise ValueError("Оъем стиральной машины должен быть положительным числом")
        self.value = value

        if not isinstance(occupied_value, (int, float)):
            raise TypeError("Объем занимаемый вещами должен быть типа int или float")
        if occupied_value < 0:
            raise ValueError("Объем занимаемый вещами не должен быть отрицательным числом")
        self.occupied_value = occupied_value

    def is_empty_washer(self) -> bool:
        """
        Функция которая проверяет является ли стриальная машина пустой
        :return: Является ли стриальная машина пустой
        Примеры:
        >>> washer = Washer(30, 10).is_empty_washer()
        """
        ...

    def reduce_occuiped_value_to_washer(self, reduce_occuiped_value: float) -> None:
        """
        Уменьшения объема занимаемый вещами.
        :param reduce_occuiped_value: Площадь уменьшаемой площади
        :raise ValueError: Если уменьшаемый объема превышает объема занимаемый вещами, то вызываем ошибку
        Примеры:
        >>> washer = Washer(80, 9600)
        >>> washer.reduce_occuiped_value_to_washer(5)
        """
        if not isinstance(reduce_occuiped_value, (int, float)):
            raise TypeError("Уменьшаемsq объем должн быть типа int или float")
        if reduce_occuiped_value < 0:
            raise ValueError("Уменьшаемый объем не должн быть отрицательным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
