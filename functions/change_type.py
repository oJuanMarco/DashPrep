#import de funções de limpar tela, questionario pra limitar opções do usuario e pandas para uso das funções da lib
from functions.clear_screen import clear_screen
import questionary
import pandas as pd

def change_column_type(query):
    # iteração por coluna da tabela
    for column in query.columns:
        # print de infos para view do usuário
        print(f"{column}")
        print(f"Tipo atual: {query[column].dtype}")
        print(f"Exemplo de dados: \n{query[column].iloc[1:4]}")
        
        # pergunta em que o usuário decide se irá trocar object tipo string da coluna
        resposta = questionary.select('Deseja alterar o tipo da coluna?',choices = ['não','sim']).ask()
        if resposta == 'não':
            pass
        else:
            # se selecionar sim, escolhe entre int, float ou date
            resposta = questionary.select('Por qual tipo?',choices = ['integer','float','date']).ask()
            match resposta:
                # se seleciona int ou float, 1º passa pra numerico e então para o valor especificado, para caso de erro, virar NaN
                case "integer":
                    query[column] = pd.to_numeric(query[column],errors='coerce')
                    query[column] = query[column].astype(int,copy=True, errors='raise')
                    input(f"Novo tipo: {query[column].dtype}")
                case "float":
                    query[column] = pd.to_numeric(query[column],errors='coerce')
                    query[column] = query[column].astype(float,copy=True, errors='raise')
                    input(f"Novo tipo: {query[column].dtype}")
                # se escolhe date, a função aceita qualquer padrao 
                case _:
                    query[column] = pd.to_datetime(query[column],format='mixed',errors='coerce')
                    input(f"Novo tipo: {query[column].dtype}")

        clear_screen()

    return query