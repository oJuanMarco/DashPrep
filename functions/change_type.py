# aqui tera 2 funções, outra pro tipo desejado
from functions.clear_screen import clear_screen
import questionary
import pandas as pd

def change_column_type(query):
    for column in query.columns:
        
        print(f"{column}")
        print(query[column].dtype)

        while True:
            resposta = questionary.select('Deseja alterar o tipo da coluna?',choices = ['sim','não']).ask()
            if resposta == 'não':
                break
            else:
                resposta = questionary.select('Por qual tipo?',
                                                choices = ['integer','float','data']).ask()
                match resposta:
                    case "integer":
                        query[column] = pd.to_numeric(query[column],errors='coerce')
                        query[column] = query[column].astype(int,copy=True, errors='raise')
                        break
                    case "float":
                        query[column] = pd.to_numeric(query[column],errors='coerce')
                        query[column] = query[column].astype(float,copy=True, errors='raise')
                        break
                    case _:
                        query[column] = pd.to_datetime(query[column],format='mixed',errors='coerce')
                        break

        input(f"Novo tipo: {query[column].dtype}")
        clear_screen()

    return query