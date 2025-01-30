class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __str__(self):
        return super().__str__() + f". Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return super().__str__() + f". Длительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == "__main__":
    # Создаем бумажную книгу
    paper_book = PaperBook(name="Гарри Поттер", author="Дж. К. Роулинг", pages=500)
    print(paper_book)  # Должно вывести информацию о книге

    # Создаем аудиокнигу
    audio_book = AudioBook(name="1984", author="Джордж Оруэлл", duration=11.5)
    print(audio_book)  # Должно вывести информацию о книге

    # Проверка, что name и author нельзя изменить
    try:
        paper_book.name = "Другой Гарри Поттер"
    except AttributeError as e:
        print(e)  # Должно вывести ошибку

    # Проверка setter'ов для pages и duration
    try:
        paper_book.pages = -100
    except ValueError as e:
        print(e)  # Должно вывести ошибку

    try:
        audio_book.duration = "долго"
    except ValueError as e:
        print(e)  # Должно вывести ошибку
