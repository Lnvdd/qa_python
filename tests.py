import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_two_books_count_is_two(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name, expected_count", [
        ("", 0),
        ("a" * 41, 0),
    ])
    def test_add_book_with_empty_name_not_added(self, collector, book_name, expected_count):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_count

    @pytest.mark.parametrize("book_name", [
        "Властелин колец",
        "Гарри Поттер",
        "1984",
    ])
    def test_add_duplicate_book_not_duplicate_count(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_first_set(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Детективы')
        assert collector.get_book_genre('Дюна') == 'Детективы'

    def test_set_book_genre_change_to_another(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Детективы')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') is None

    def test_get_book_genre_empty_initially(self, collector):
        collector.add_new_book('Пикник на обочине')
        assert collector.get_book_genre('Пикник на обочине') == ''

    def test_get_book_genre_after_setting(self, collector):
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Комедии')
        assert collector.get_book_genre('Пикник на обочине') == collector.books_genre['Пикник на обочине']

    def test_get_book_genre_for_nonexistent_book(self, collector):
        assert collector.get_book_genre('Скотный двор') is None

    def test_get_books_with_specific_genre_contains_only_right_books(self, collector):
        collector.add_new_book('Дракула')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.set_book_genre('Горе от ума', 'Комедии')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Дракула' in books and 'Горе от ума' not in books

    def test_get_books_with_specific_genre_no_books(self, collector):
        assert collector.get_books_with_specific_genre('Драма') == []

    def test_get_all_books_genres(self, collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Мультфильмы')
        collector.add_new_book('451 градус по Фаренгейту')
        assert collector.get_books_genre() == {'Ведьмак': 'Мультфильмы', '451 градус по Фаренгейту': ''}

    def test_get_books_for_children_includes_and_excludes_correctly(self, collector):
        collector.add_new_book('Приключения Паддингтона')
        collector.set_book_genre('Приключения Паддингтона', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        child_books = collector.get_books_for_children()
        assert 'Приключения Паддингтона' in child_books and 'Оно' not in child_books

    def test_add_book_in_favorites_only_once(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books().count('Шерлок Холмс') == 1

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Мастера и Маргарита')
        collector.add_book_in_favorites('Мастера и Маргарита')
        collector.delete_book_from_favorites('Мастера и Маргарита')
        assert 'Мастера и Маргарита' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_with_nonexistent_book(self, collector):
        collector.delete_book_from_favorites('Нет такой книги')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_initially_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_after_adding(self, collector):
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        assert collector.get_list_of_favorites_books() == ['Хоббит']
