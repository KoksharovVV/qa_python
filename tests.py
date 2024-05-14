import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name, res', (
            ['Lorem ipsum dolor sit amet, consectetuer.', 0],
            ['', 0],
            ['123', 1]
    ))
    def test_add_new_book_add_book_with_different_name_lenghts(self, collector, name, res):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == res

    def test_set_book_genre_set_existing_genre(self, collector, book):
        collector.set_book_genre('Наименование', 'Ужасы')
        assert collector.books_genre['Наименование'] == 'Ужасы'

    @pytest.mark.parametrize('name, genre, res', (
            ['Наименование', "Ужасы", "Ужасы"],
            ['Lorem ipsum dolor sit amet, consectetuer.', 'Фантастика', None],
            ['Наименование', "Жанр", '']
    ))
    def test_get_book_genre(self, collector, name, genre, res):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == res

    @pytest.mark.parametrize('name, genre, res', (
            ['Наименование', "Ужасы", ['Наименование']],
            ['Lorem ipsum dolor sit amet, consectetuer.', 'Фантастика', []],
            ['Наименование', "Жанр", []]
    ))
    def test_get_books_with_specific_genre(self, collector, name, genre, res):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == res

    def test_get_books_genre_empty_books_genre(self, collector):
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('name, genre, res', (
            ['Наименование', 'Ужасы', {'Наименование': 'Ужасы'}],
            ['Наименование', 'genre', {'Наименование': ''}]
    ))
    def test_get_books_genre(self, collector, name, genre, res):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == res

    @pytest.mark.parametrize('name, genre, res', (
            ['Наименование', 'Ужасы', []],
            ['Наименование', None, []],
            ['Наименование', 'Мультфильмы', ['Наименование']]
    ))
    def test_get_books_for_children(self, collector, name, genre, res):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == res

    @pytest.mark.parametrize('name, genre, res', (
            ['Наименование', 'Ужасы', ['Наименование']],
            ['Наименование', None, ['Наименование']],
            ['Наименование', 'Мультфильмы', ['Наименование']]
    ))
    def test_add_book_in_favorites(self, collector, name, genre, res):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert collector.favorites == res

    @pytest.mark.parametrize('name, delete, res', (
            ['Наименование', 'Наименование', []],
            ['Наименование', None, ['Наименование']]
    ))
    def test_delete_book_from_favorites(self, collector, name, delete, res):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(delete)
        assert collector.favorites == res

    @pytest.mark.parametrize('name, res', (
            ['Наименование', ['Наименование']],
            ['', []]
    ))
    def test_get_list_of_favorites_books(self, collector, name, res):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == res
