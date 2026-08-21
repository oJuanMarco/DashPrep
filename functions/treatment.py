from functions.blank_space_remove import blank_space_remove
from functions.list_colunms import list_colunms
from functions.remove_char import char_remove
from functions.change_colunm_name import change_colunm_name

def treatment(query):
    
    treat_1 = blank_space_remove(query)
    treat_2 = change_colunm_name(treat_1)
    # treat_3 = char_remove(treat_2)

    input(query)
    