from functions.blank_space_remove import blank_space_remove
from functions.list_colunms import list_colunms
from functions.remove_char import char_remove

# importar os pra ir limpando tela durante a config

def treatment(query):
    
    treat_1 = blank_space_remove(query)
    treat_2 = char_remove(treat_1)

    input(query)
    