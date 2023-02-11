class FruitTree:
    def __init__(self,  name: str, fruit: str, number_of_fruit: int):
        """
        Создание базового класса плодового дерева
        :param name: название дерева
        :param fruit: название плода дерева
        :param number_of_fruit: количество плодов на дереве
        """
        if not isinstance(name, str):
            raise TypeError('Название дерева должно быть типа str')
        self.name = name
        if not isinstance(name, str):
            raise TypeError('Название плода дерева должно быть типа str')
        self.fruit = fruit
        if not isinstance(number_of_fruit, int):
            raise TypeError('Количество плодов на дереве должно быть типа int')
        if number_of_fruit < 0:
            raise ValueError('Количество плодов на дереве должно быть неотрицательным числом')
        self.number_of_fruit = number_of_fruit

    def fruit_on_the_tree(self, fallen_fruit: int) -> int:
        """
        Определение количества оставшихся фруктов на дереве
        :param fallen_fruit: упавшие фрукты
        """
        if not isinstance(fallen_fruit, int):
            raise TypeError('Количество упавших фруктов должно быть типа int')
        if fallen_fruit < 0:
            raise ValueError('Количество упавших фруктов должно быть неотрицательным числом')
        return self.number_of_fruit - fallen_fruit

    def Cheburashka(self,  fallen_fruit: int, capacity_of_the_basket: int) -> int:
        """
        Чебурашка собирает в корзину фрукты, упавшие с дерева.
        Определение количества нужных корзин.
        :param fallen_fruit: упавшие фрукты
        :param capacity_of_the_basket: вместимость корзины
        """
        if not isinstance(fallen_fruit, int):
            raise TypeError('Количество упавших фруктов должно быть типа int')
        if fallen_fruit < 0:
            raise ValueError('Количество упавших фруктов должно быть неотрицательным числом')
        if not isinstance(capacity_of_the_basket, int):
            raise TypeError('Вместимость корзины должно быть типа int')
        if capacity_of_the_basket <= 0:
            raise ValueError('Вместимость корзины должно быть положительным числом')
        ...

    def __str__(self):
        return f"Плодовое дерево: {self.name}. Плод: {self.fruit}. Количество плодов на дереве: {self.number_of_fruit}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, fruit={self.fruit!r}, number_of_fruit={self.number_of_fruit!r})"


class AppleTree(FruitTree):
    def __init__(self, name: str, fruit: str, number_of_fruit: int, fruit_color: str):
        super().__init__(name, fruit, number_of_fruit)
        self.fruit_color = fruit_color

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, fruit={self.fruit!r}, number_of_fruit={self.number_of_fruit!r}, fruit_color={self.fruit_color!r})"


class OrangeTree(FruitTree):
    def __init__(self, name: str, fruit: str, number_of_fruit: int):
        super().__init__(name, fruit, number_of_fruit)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, fruit={self.fruit!r}, number_of_fruit={self.number_of_fruit!r})"

    def Cheburashka (self,  fallen_fruit: int, capacity_of_the_basket: int) -> int:
        """
        Перегрузка метода, так как плоды являются апельсинами (Чебурашка очень любит апельсины)
        Чебурашка собирает в корзину и упавшие с дерева фрукты, и висящие на дереве.
        Определение количества нужных корзин.
        :param fallen_fruit: упавшие фрукты
        :param fruit_on_the_tree: фрукты на дереве
        :param capacity_of_the_basket: вместимость корзины
        """
        if not isinstance(fallen_fruit, int):
            raise TypeError('Количество упавших фруктов должно быть типа int')
        if fallen_fruit < 0:
            raise ValueError('Количество упавших фруктов должно быть неотрицательным числом')
        if not isinstance(capacity_of_the_basket, int):
            raise TypeError('Вместимость корзины фруктов должно быть типа int')
        if capacity_of_the_basket <= 0:
            raise ValueError('Вместимость корзины должно быть положительным числом')
        ...


if __name__ == "__main__":
    fruit_tree_1 = AppleTree('Яблоня', 'яблоко', 40, 'красный')
    print(fruit_tree_1.__repr__())
    print(fruit_tree_1.fruit_on_the_tree(10))
    pass
