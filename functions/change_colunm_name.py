# função recebe nomes de colunas e as modifica
from functions.clear_screen import clear_screen

# função pra remover caracteres informados para cada coluna
def change_colunm_name(query):

    colunas = []
    print(f"Lista de colunas da tabela:\n")
    for colunm in query.columns:

        colunm = f'{colunm}'.lower().replace(" ","_")
        # atrelar a um dicionario e usar rename
        print(f"-{colunm}")
        colunas.append(colunm)

    print("\n")
    
    i=0

    while True:
        resposta = input("Deseja alterar algum/outro dos titulos listados?(y/n): ").lower()
        if resposta == 'y' or resposta=='n':
            if resposta == 'n':
                break
            else:
                while i<=0 or i>len(colunas):
                    i=int(input(f"Informe qual a posição (1-{len(colunas)}), de baixo pra cima, do título que deseja alterar: "))

                mudanca = input(f"Informe o nome novo de {colunas[i-1]} ('branco' pra removê-los e 'minusculo' para padronizar) - ").lower()

                i = 0

                for colunm in query.columns:
                    if colunm == colunas[i-1]:
                        colunm = mudanca.lower().replace(" ","_")
                        print('\n')
                        break
                    else:
                        pass
                
        else:
            print("Informe somente 'y' ou 'n'\n")
        
    clear_screen()
    
    colunas = []
    return query