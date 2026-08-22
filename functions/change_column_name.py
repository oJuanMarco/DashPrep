# função recebe nomes de colunas e as modifica
from functions.clear_screen import clear_screen

# função pra remover caracteres informados para cada coluna
def change_column_name(query):

    colunas = []

    print(f"Lista de colunas da tabela:\n")
    for column in query.columns:

        column = f'{column}'.lower().replace(" ","_")
        print(f"-{column}")
        colunas.append(column)

    print("\n")
    
    i=0

    while True:
        resposta = input("Deseja alterar algum/outro dos titulos listados?(y/n): ").lower()
        if resposta == 'y' or resposta=='n':
            if resposta == 'n':
                break
            else:
                while i<=0 or i>len(colunas):
                    try:
                        i=int(input(f"Informe qual a posição (1-{len(colunas)}), de baixo pra cima, do título que deseja alterar: "))
                    except ValueError:
                        print("Informe somente os números de posição")
                mudanca = input(f"Informe o nome novo de {colunas[i-1]} - ").lower()

                for elemento in colunas:
                    if elemento == colunas[i-1]:
                        j=0
                        for column in query.columns:
                            if j == i-1:
                                query.rename(columns={query.columns[j]:mudanca.replace(" ","_").strip()},inplace=True)
                                print(f"{column} trocada por {mudanca}")
                                break
                            else:
                                j+=1
                                print(f"Erro {j}")
                        print('\n')
                        break
                    else:
                        print(f"Elemento não encontrado")        
                
                i = 0
        else:
            print("Informe somente 'y' ou 'n'\n")
        
    clear_screen()
    
    colunas = []
    return query