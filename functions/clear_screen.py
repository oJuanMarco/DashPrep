# função para limpar tela do terminal para evitar poluição durante seleções manuais

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")