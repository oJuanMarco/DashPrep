# esta função é a principal na parte de tratamento, chama todas as ordem na ordem estipulada para tratamento manual precisa
from functions.blank_space_remove import blank_space_remove
from functions.change_column_name import change_column_name
from functions.change_char import char_change
from functions.remove_char import char_remove
from functions.change_type import change_column_type
from functions.clear_screen import clear_screen

def treatment(query):
    treat_1 = blank_space_remove(query)
    treat_2 = change_column_name(treat_1)
    treat_3 = char_change(treat_2)
    treat_4 = char_remove(treat_3)
    treat_5 = change_column_type(treat_4)

    input(query)
    clear_screen()
    return treat_5    