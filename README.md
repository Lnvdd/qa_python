# qa_python
test_add_two_books_count_is_two
Проверяет, что после добавления двух книг их количество становится ровно два

test_add_book_with_empty_name_not_added
Проверяет, что книга с пустым названием или слишком длинным названием не добавляется

test_add_duplicate_book_not_duplicate_count
Проверяет, что нельзя добавить одну и ту же книгу дважды

test_set_book_genre_first_set
Проверяет, что можно успешно установить жанр для книги в первый раз

test_set_book_genre_change_to_another
Проверяет, что жанр книги можно изменить на другой

test_set_genre_for_nonexistent_book
Проверяет, что жанр не устанавливается для книги, которой нет в списке

test_get_book_genre_empty_initially
Проверяет, что у новой книги жанр по умолчанию пустой

test_get_book_genre_after_setting
Проверяет, что метод возвращает правильный жанр после установки

test_get_book_genre_for_nonexistent_book
Проверяет, что для несуществующей книги жанр не найден (возвращается None)

test_get_books_with_specific_genre_contains_only_right_books
Проверяет, что возвращаются только книги с указанным жанром

test_get_books_with_specific_genre_no_books
Проверяет, что если книг с указанным жанром нет, возвращается пустой список

test_get_all_books_genres
Проверяет, что возвращается весь словарь книг с их жанрами

test_get_books_for_children_includes_and_excludes_correctly
Проверяет, что книги с детским жанром включаются, а с возрастным ограничением исключаются

test_add_book_in_favorites_only_once
Проверяет, что книга добавляется в избранное только один раз

test_delete_book_from_favorites_removes_book
Проверяет, что книга успешно удаляется из избранного

test_delete_book_from_favorites_with_nonexistent_book
Проверяет, что попытка удалить отсутствующую книгу из избранного не вызывает ошибок

test_get_list_of_favorites_initially_empty
Проверяет, что список избранных книг пуст при старте

test_get_list_of_favorites_after_adding
Проверяет, что добавленная книга появляется в списке избранных