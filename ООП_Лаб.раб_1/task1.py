import doctest


class Bus:
    def __init__(self, number_of_seats: int, route_number: str, time_interval: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param number_of_seats: Количество лампочек
        :param route_number: Длина гирлянды
        :param time_interval: Цвет лампочек гирлянды

        Примеры:
        >>> bus = Bus(50, '39э', 15) #инициализация экземляра класса
        """
        self.number_of_seats = number_of_seats
        self.route_number = route_number
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
        self.amount_lamps = amount_lamps
        self.length = length
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
        self.height = height
        self.width = width
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
