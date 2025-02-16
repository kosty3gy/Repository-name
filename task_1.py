from datetime import datetime


class Transport:
    """
    Базовый класс для всех транспортных средств.

    Attributes:
        brand (str): Производитель транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """Инициализация атрибутов транспортного средства."""
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление транспортного средства."""
        return f"Transport(make='{self._brand}', model='{self._model}', year={self._year})"

    def get_age(self) -> int:
        """Возвращает возраст транспортного средства."""
        current_year = datetime.now().year
        return current_year - self._year


### Дочерний класс: Car


class Car(Transport):
    """
    Класс для легковых автомобилей, наследующий от Transport.

    Attributes:
        number_of_doors (int): Количество дверей в автомобиле.
    """

    def __init__(self, brand: str, model: str, year: int, number_of_doors: int) -> None:
        """Инициализация атрибутов легкового автомобиля."""
        super().__init__(brand, model, year)  # Унаследуем инициализацию родительского класса
        self.number_of_doors = number_of_doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} с {self.number_of_doors} дверями"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление легкового автомобиля."""
        return f"Car(make='{self._brand}', model='{self._model}', year={self._year}, number_of_doors={self.number_of_doors})"

    def get_age(self) -> int:
        """Возвращает возраст легкового автомобиля с учетом специальной отметки."""
        age = super().get_age()
        if age > 10:
            print("Это автомобиль старше 10 лет.")
        return age


### Дочерний класс: Motorcycle


class Motorcycle(Transport):
    """
    Класс для мотоциклов, наследующий от Transport.

    Attributes:
        type (str): Тип мотоцикла.
    """

    def __init__(self, brand: str, model: str, year: int, type: str) -> None:
        """Инициализация атрибутов мотоцикла."""
        super().__init__(brand, model, year)  # Унаследуем инициализацию родительского класса
        self._type = type

    def __str__(self) -> str:
        """Возвращает строковое представление мотоцикла."""
        return f"{super().__str__()} - тип: {self._type}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление мотоцикла."""
        return f"Motorcycle(make='{self._brand}', model='{self._model}', year={self._year}, type='{self._type}')"


# Примеры использования классов
car = Car("Toyota", "Camry", 2015, 4)
motorcycle = Motorcycle("Yamaha", "YZF-R1", 2020, "спорт")


if __name__ == "__main__":
    print(car)  # Вывод: Toyota Camry (2015) с 4 дверями
    print(repr(car))  # Вывод: Car(make='Toyota', model='Camry', year=2015, number_of_doors=4)
    print(car.get_age())  # Возраст автомобиля

    print(motorcycle)  # Вывод: Yamaha YZF-R1 (2020) - тип: спорт
    print(repr(motorcycle))  # Вывод: Motorcycle(make='Yamaha', model='YZF-R1', year=2020, type='спорт')

