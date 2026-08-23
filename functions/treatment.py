from functions.blank_space_remove import blank_space_remove
from functions.change_column_name import change_column_name
from functions.remove_char import char_remove
from functions.clear_screen import clear_screen

def treatment(query):
    
    treat_1 = blank_space_remove(query)
    treat_2 = change_column_name(treat_1)
    treat_3 = char_remove(treat_2)

    input(query)
    clear_screen()    