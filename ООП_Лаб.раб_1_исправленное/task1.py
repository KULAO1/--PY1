import doctest


class Bus:
    def __init__(self, number_of_seats: int, route_number: str, time_interval: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param number_of_seats: Количество мест в автобусе
        :param route_number: Номер маршрута
        :param time_interval: Интервал отправления автобусов

        Примеры:
        >>> bus = Bus(50, '39э', 15) #инициализация экземляра класса
        """
        if not isinstance(number_of_seats, int):
            raise TypeError("Количество мест в автобусе должно быть типа int")
        if number_of_seats <= 0:
            raise ValueError("Количество мест в автобусе должно быть положительным числом")
        self.number_of_seats = number_of_seats
        if not isinstance(route_number, str):
            raise TypeError("Номер маршрута должен быть типа str")
        self.route_number = route_number
        if not isinstance(time_interval, int):
            raise TypeError("Интервал отправления автобусов должен быть типа int")
        if number_of_seats <= 0:
            raise ValueError("Интервал отправления автобусов должен быть положительным числом")
        self.time_interval = time_interval

    def available_seats(self, number_of_people_in_the_bus: int, people_who_came: int, exited_people: int) -> int:
        """
        Нахождение количества свободных мест в автобусе
        :param number_of_people_in_the_bus: Количество людей, находящихся в автобусе
        :param people_who_came: Количество вошедших людей
        :param exited_people: Количество вышедших людей

        :return: Количество свободных мест

        Примеры:
        >>> bus = Bus(50, '39э', 15)
        >>> bus.available_seats(23, 5, 2)
        """
        if not isinstance(number_of_people_in_the_bus, int):
            raise TypeError("Количество людей, находящихся в автобусе, должно быть типа int")
        if number_of_people_in_the_bus < 0:
            raise ValueError("Количество людей, находящихся в автобусе, должно быть положительным числом")
        if not isinstance(people_who_came, int):
            raise TypeError("Количество вошедших людей должно быть типа int")
        if people_who_came < 0:
            raise ValueError("Количество вошедших людей должно быть положительным числом")
        if not isinstance(exited_people, int):
            raise TypeError("Количество вышедших людей должно быть типа int")
        if exited_people < 0:
            raise ValueError("Количество вышедших людей должно быть положительным числом")
        ...

    def route_correctness(self) -> bool:
        """
        Проверка номера маршрута автобуса пассажиром

        :return: Является ли данный маршрут нужным

        Примеры:
        >>> bus = Bus(50, '39э', 15)
        >>> bus.route_correctness()
        """
        ...


class Garland:
    def __init__(self, amount_lamps: int, length: int, color: str):
        """
        Создание и подготовка к работе объекта "Гирлянда"

        :param amount_lamps: Количество лампочек
        :param length: Длина гирлянды
        :param color: Цвет лампочек гирлянды

        Примеры:
        >>> garland = Garland(30, 1400, 'белый') #инициализация экземляра класса
        """
        if not isinstance(amount_lamps, int):
            raise TypeError("Количество лампочек должно быть типа int")
        if amount_lamps <= 0:
            raise ValueError("Количество лампочек должно быть положительным числом")
        self.amount_lamps = amount_lamps
        if not isinstance(length, int):
            raise TypeError("Длина гирлянды должна быть типа int")
        if length <= 0:
            raise ValueError("Длина гирлянды должна быть положительным числом")
        self.length = length
        if not isinstance(color, str):
            raise TypeError("Цвет лампочек гирлянды должен быть типа str")
        self.color = color

    def broken_lamps(self, serviceable_lamps: int) -> int:
        """
        Нахождение количества сгоревших лампочек
        :param serviceable_lamps: Количество исправных лампочек

        :return: Количество сломанных лампочек

        Примеры:
        >>> garland = Garland(30, 1400, 'белый')
        >>> garland.broken_lamps(22)
        """
        if not isinstance(serviceable_lamps, int):
            raise TypeError("Количество исправных лампочек должно быть типа int")
        if serviceable_lamps < 0:
            raise ValueError("Количество исправных лампочек должно быть положительным числом")
        ...

    def decorate_the_room(self, length_room: int, width_room: int) -> bool:
        """
        Проверка: хватит ли длины гирлянды, чтобы протянуть ее по периметру комнаты?
        :param length_room: Длина комнаты
        :param width_room: Ширина комнаты

        :return: Хватает ли длины гирлянды

        Примеры:
        >>> garland = Garland(30, 1400, 'белый')
        >>> garland.decorate_the_room(4, 3)
        """
        if not isinstance(length_room, int):
            raise TypeError("Длина комнаты должна быть типа int")
        if length_room <= 0:
            raise ValueError("Длина комнаты должна быть положительным числом")
        if not isinstance(width_room, int):
            raise TypeError("Ширина комнаты должна быть типа int")
        if width_room <= 0:
            raise ValueError("Ширина комнаты должна быть положительным числом")
        ...


class Closet:
    def __init__(self, height: int, width: int, depth: int):
        """
        Создание и подготовка к работе объекта "Шкаф"
        
        :param height: Высота шкафа
        :param width: Ширина шкафа
        :param depth: Глубина шкафа
        
        Примеры:
        >>> closet = Closet(200, 100, 50) #инициализация экземляра класса
        """
        if not isinstance(height, int):
            raise TypeError("Высота шкафа должна быть типа int")
        if height <= 0:
            raise ValueError("Высота шкафа должна быть положительным числом")
        self.height = height
        if not isinstance(width, int):
            raise TypeError("Ширина шкафа должна быть типа int")
        if width <= 0:
            raise ValueError("Ширина шкафа должна быть положительным числом")
        self.width = width
        if not isinstance(depth, int):
            raise TypeError("Глубина шкафа должна быть типа int")
        if depth <= 0:
            raise ValueError("Глубина шкафа должна быть положительным числом")
        self.depth = depth

    def volume_of_closet(self) -> int:
        """
        Нахождение объёма шкафа

        :return: Объём шкафа

        Примеры:
        >>> closet = Closet(200, 100, 50)
        >>> closet.volume_of_closet()
        """
        ...

    def door_area(self) -> int:
        """
        Нахождение площади дверцы шкафа

        :return: Площадь дверцы шкафа

        Примеры:
        >>> closet = Closet(200, 100, 50)
        >>> closet.door_area()
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()
    pass
