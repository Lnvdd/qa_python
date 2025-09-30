# qa_python
test_add_two_books_count_is_two
Проверка, что добавление двух книг увеличивает количество книг до двух

test_add_book_with_empty_name_not_added
Проверка, что книга с пустым названием или длиной больше 40 символов не добавляется

test_add_duplicate_book_not_duplicate_count
Проверка, что при добавлении книги-дубликата количество книг не увеличивается

test_set_book_genre_first_set
Проверка успешного начального присвоения жанра книге

test_set_book_genre_change_to_another
Проверка изменения жанра книги на другой жанр

test_set_genre_for_nonexistent_book
Проверка, что жанр не устанавливается для несуществующей книги

test_get_book_genre_empty_initially
Проверка, что у ново добавленной книги жанр по умолчанию пустой

test_get_book_genre_after_setting
Проверка, что возвращается корректный жанр после установки

test_get_book_genre_for_nonexistent_book
Проверка, что для отсутствующей в коллекции книги жанр возвращается None

test_get_books_with_specific_genre_contains_only_right_books
Проверка корректного поиска и возврата книг с указанием конкретного жанра

test_get_books_with_specific_genre_no_books
Проверка, что при отсутствии книг с заданным жанром возвращается пустой список

test_get_all_books_genres
Проверка корректного возврата полного словаря всех книг и их жанров

test_get_books_for_children_includes_and_excludes_correctly
Проверка фильтрации детских книг: включение неимеющих возрастного рейтинга жанров и исключение с возрастным рейтингом

test_add_book_in_favorites_only_once
Проверка, что книга добавляется в избранное только один раз

test_delete_book_from_favorites_removes_book
Проверка успешного удаления книги из списка избранных

test_delete_book_from_favorites_with_nonexistent_book
Проверка, что удаление несуществующей книги из фаворитов не вызывает ошибок и не влияет на список

test_get_list_of_favorites_initially_empty
Проверка, что список избранных книг пуст изначально

test_get_list_of_favorites_after_adding
Проверка, что книга корректно добавляется в список избранных