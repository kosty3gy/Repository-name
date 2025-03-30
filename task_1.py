import doctest


class Circle:
    def __init__(self, square: float, perimeter: float):
        """
        Определение параметров круга

        :param  square: Площадь круга
        :param perimeter: Периметр круга

        Примеры:
        >>> сircle_1 = Circle(500, 300)  # инициализация экземпляра класса
        """
        if not isinstance(square, (int, float)):
            raise TypeError("Площадь круга должен быть типа int или float")
        if square <= 0:
            raise ValueError("Площадь круга должен быть положительным числом")
        self.square = square

        if not isinstance(perimeter, (int, float)):
            raise TypeError("Периметр круга должно быть int или float")
        if perimeter < 0:
            raise ValueError("Периметр круга не может быть отрицательным ым числом")
        self.perimeter = perimeter

    def finding_the_radius(self, square: float):
        """
        Нахождение радиуса.

        :param square: Площадь круга

        :return: радиус окружности

        Примеры:
        >>> сircle_1 = Circle(500, 300)
        >>> сircle_1.finding_the_radius(500)
        """
        ...

    def increasing_the_parameters(self, radius: float) -> None:
        """
        Нахождение обновлённых параметров.

        :param radius: радиус круга

        :return: Площадь круга
        :return: Периметр круга

        Примеры:
        >>> сircle_1 = Circle(500, 300)
        >>> сircle_1.increasing_the_parameters(10)
        """
        ...


class Fire:
    def __init__(self, temperature: float, time: float):
        """
        Горение и его параметры.

        :param  temperature: температура огня
        :param time: время горения

        Примеры:
        >>> fire = Fire(500, 300)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("температура огня должна быть типа int или float")
        if temperature <= 0:
            raise ValueError("температура огня должна  быть положительным числом")
        self.temperature = temperature

        if not isinstance(time, (int, float)):
            raise TypeError("время горения должно быть int или float")
        if time < 0:
            raise ValueError("время горения не может быть отрицательным числом")
        self.time = time

    def the_object_gorenje(self):
        """
        Предмет горения.

        :param square: предмет горения

        :return: запись материала

        Примеры:
        >>> fire = Fire(500, 300)
        >>> fire.the_object_gorenje('дерево')
        """
        ...

    def heat_generated(self, temperature: float, time: float) -> None:
        """
        Нахождения колличества тепла.

        :param  temperature: температура огня
        :param time: время горения

        :return: выделенное тепло

        Примеры:
        >>> fire = Fire()
        >>> fire.heat_generated(500, 300)
        """
        ...


class Ice:
    def __init__(self, temperature: float, time: float):
        """
        Замерзание и его свойства

        :param  temperature: температура замерзания
        :param time: время замерзания

        Примеры:
        >>> ice = Ice(500, 300)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("температура замерзания должна быть типа int или float")
        self.temperature = temperature

        if not isinstance(time, (int, float)):
            raise TypeError("время замерзания должно быть int или float")
        if time < 0:
            raise ValueError("время замерзания не может быть отрицательным числом")
        self.time = time

    def the_object_ice(self):
        """
        объект замерзания

        :param square: предмет замерзания

        :return: запись материала

        Примеры:
        >>> ice = Ice()
        >>> ice.the_object_gorenje('water')
        """
        ...

    def heat_absorbing(self, temperature: float, time: float) -> None:
        """
        Нахождения колличества тепла.

        :param  temperature: температура замерзания
        :param time: время замерзания

        :return: выделенное тепло

        Примеры:
        >>> ice = Ice()
        >>> ice.heat_absorbing('water')
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
