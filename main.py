class MusicalInstrument:
    """Базовый класс музыкального инструмента"""
    def __init__(self, name: str, weight: int):
        self._name = name
        self.weight = weight # вес в граммах

    @property # применено для того, чтобы сделать атрибут только для чтения
    def name(self) -> str:
        return self._name

    @property # применено для setter
    def weight(self) -> int:
        return self._weight

    @weight.setter # применено для сокрытия и навешивания дополнительной логики
    def weight(self, new_weight: int) -> None:
        if not isinstance(new_weight, int):
            raise TypeError("Масса музыкального инструмента должна быть типа int")
        if new_weight <= 0:
            raise ValueError("Масса музыкального инструмента должна быть положительным числом")
        self._weight = new_weight

    def __str__(self):
        return f"Инструмент: {self.name}. Вес: {self.weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight}"

    def CountMass(self):
        """Метод который считает массу инструмента.
        Данный метод наследуется всеми дочерними классами, так как везде вес находится таким образом"""
        return self.weight / 1000 * 9.8

    def CountInstruments(self):
        """Метод который считает количество музыкальных интсрументов"""
        ...


class StringInstrument(MusicalInstrument):
    """Дочерный класс струнного инструмента"""
    def __init__(self, name: str, weight: int, number_of_strings: int):
        super().__init__(name, weight)
        self._number_of_strings = number_of_strings

    @property # применено для того, чтобы сделать атрибут только для чтения
    def number_of_strings(self) -> int:
        return self._number_of_strings

    def __str__(self):
        return f"{super().__str__()}. Количество струн: {self.number_of_strings}."

    def __repr__(self):
        return f"{super().__repr__()}, number_of_strings={self.number_of_strings}"

    def CountInstruments(self):
        """Метод который считает количество струнных музыкальных интсрументов.
        Данный метод был перегружен, так как нам нужно именно количество струных музыкальных инструментов"""
        ...


class KeyboardInstrument(MusicalInstrument):
    """Дочерный класс клавишного инструмента"""
    def __init__(self, name: str, weight: int, number_of_keys: int):
        super().__init__(name, weight)
        self._number_of_keys = number_of_keys

    @property # применено для того, чтобы сделать атрибут только для чтения
    def number_of_keys(self) -> int:
        return self._number_of_keys

    def __str__(self):
        return f"{super().__str__()}. Количество клавиш: {self.number_of_keys}."

    def __repr__(self):
        return f"{super().__repr__()}, number_of_keys={self.number_of_keys}"

    def CountInstruments(self):
        """Метод который считает количество клавишных музыкальных интсрументов.
        Данный метод был перегружен, так как нам нужно именно количество клавишных музыкальных инструментов"""
        ...

if __name__ == "__main__":
    musical_instrument = MusicalInstrument('Скрипка', 55)
    print(musical_instrument)
    string_instrument = StringInstrument('Гитара', 5000, 6)
    print(string_instrument)
    keyboard_instrument = KeyboardInstrument('Фортепиано', 340000, 88)
    print(keyboard_instrument)
    print(string_instrument.CountMass())
    pass