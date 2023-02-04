class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, another_pages: int):
        if isinstance(another_pages, int):
            raise TypeError("Количество станиц должно быть int типа")
        if another_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = another_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, another_duration: float):
        if isinstance(another_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть float типа")
        if another_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = another_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
