# qa_python
test_add_two_books_count_is_two
Проверка, что добавление двух книг увеличивает количество книг до двух

test_add_book_with_empty_name_not_added
Проверка, что книга с пустым названием не добавляется

test_add_duplicate_book_not_duplicate_count
Проверка, что при добавлении книги-дубликата количество книг не увеличивается

test_set_book_genre_first_set
Проверка успешного начального присвоения жанра

test_set_book_genre_change_to_another
Проверка изменения жанра на другой

test_set_book_genre_cannot_change_to_third
Проверка невозможности изменить жанр на третий

test_set_genre_for_nonexistent_book
Проверка, что жанр не устанавливается для несуществующей книги

test_get_book_genre_empty_initially
Проверка, что у новой книги жанр по умолчанию пуст

test_get_book_genre_after_setting
Проверка корректного возвращения заданного жанра

test_get_book_genre_for_nonexistent_book
Проверка, что для отсутствующей книги жанр возвращается как None

test_get_books_with_specific_genre_contains_only_right_books
Проверка правильного поиска книг по жанру

test_get_books_with_specific_genre_no_books
Проверка, что при отсутствии книг заданного жанра возвращается пустой список

test_get_all_books_genres
Проверка получения словаря всех книг с их жанрами

test_get_books_for_children_includes_and_excludes_correctly
Проверка фильтрации детских книг: включение мультфильмов, исключение ужасов
             
test_add_book_in_favorites_only_once
Проверка, что книга добавляется в избранное только один раз

test_delete_book_from_favorites_removes_book
Проверка удаления книги из избранного

test_delete_book_from_favorites_with_nonexistent_book
Проверка удаления несуществующей книги из избранного без влияния

test_get_list_of_favorites_initially_empty
Проверка, что список избранного пуст изначально

test_get_list_of_favorites_after_adding
Проверка добавления книги в список избранного                  