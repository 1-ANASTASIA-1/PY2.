from typing import Union
import doctest


# Первый класс.
class Plate:
    def __init__(self, square_plate: Union[int, float], occupied_square: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Тарелка"
        :param square_plate: Площадь тарелки
        :param occupied_square: Площадь, занимаемая едой
        Примеры:
        >>> plate = Plate(300, 50)  # инициализация экземпляра класса
        """
        if not isinstance(square_plate, (int, float)):
            raise TypeError("Площадь тарелки должена быть типа int или float")
        if square_plate < 0:
            raise ValueError("Площадь тарелки должена быть положительным числом")
        self.square_plate = square_plate

        if not isinstance(occupied_square, (int, float)):
            raise TypeError("Площадь, занимаемая едой, должна быть int или float")
        if occupied_square <= 0:
            raise ValueError("Площадь, занимаемая едой, быть положительным числом")
        self.occupied_square = occupied_square

    def is_empty_plate(self) -> bool:
        """
        Функция которая проверяет является ли тарелка пустой
        :return: Является ли тарелка пустой
        Примеры:
        >>> Plate(300, 50).is_empty_plate()
        """
        ...

    def add_food_to_plate(self, add_food: float) -> None:
        """
        Добавление еды в такрелку.
        :param food: площадь добавляемой еды
        :raise ValueError: Если площадь добавляемой еды превышает площадь тарелки, то вызываем ошибку
        Примеры:
        >>> Plate(300, 50).add_food_to_plate(100)
        """
        if not isinstance(add_food, (int, float)):
            raise TypeError("Добавляемая еда должна быть типа int или float")
        if add_food < 0:
            raise ValueError("Добавляемая еда не должна быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
