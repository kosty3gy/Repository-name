# TODO Найдите количество книг, которое можно разместить на дискете
volume_dickret = 1.44
number_page_book = 100
number_lines_page = 50
number_symbol_page = 25
one_symbol = 4

weight_book = one_symbol * number_symbol_page * number_lines_page * number_page_book / 1024**2

number_page_book = volume_dickret // weight_book

print("Количество книг, помещающихся на дискету:", int(number_page_book))
