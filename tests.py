from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_get_books_genre_empty(self): #получение пустого списка жанров
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
    def test_add_new_book_invalid_long_name(self): #добавление книги с длинным названием
        collector = BooksCollector()
        invalid_name = "test"*11
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()
    def test_add_new_book_valid_name_no_genre(self): #Добавление книги без жанра
        collector = BooksCollector()
        collector.add_new_book("Маленький принц")
        assert "Маленький принц" in collector.get_books_genre()
        assert collector.get_books_genre()["Маленький принц"] == ""

    def test_set_book_genre_valid_genre(self): #Добавление корректного жанра
        collector = BooksCollector()
        collector.add_new_book("Тихий дон")
        collector.set_book_genre("Тихий дон", "Комедии")
        assert collector.get_book_genre("Тихий дон") == "Комедии"

    def test_get_books_with_specific_genre(self): #получение нужной книги по жанру
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение")
        collector.set_book_genre("Гордость и предубеждение", "Фантастика")
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Детективы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гордость и предубеждение"]
        assert collector.get_books_with_specific_genre('Детективы') == ["Война и мир"]
    def test_get_books_for_children(self): #получение детской книги
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.add_new_book("Книга не для детей")
        collector.set_book_genre("Книга не для детей", "Ужасы")
        assert collector.get_books_for_children() == ["Детская книга"]

    def test_get_list_of_favorites_books_empty(self): #получение пустого списка избранного
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites(self): #добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.set_book_genre("Любимая книга", "Комедии")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()
    def test_delete_book_from_favorites(self): #удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book("Любимая книга1")
        collector.set_book_genre("Любимая книга1", "Комедии")
        collector.add_book_in_favorites("Любимая книга1")
        collector.delete_book_from_favorites("Любимая книга1")
        assert "Любимая книга1" not in collector.get_list_of_favorites_books()












