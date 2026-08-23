# função recebe nomes de colunas e as modifica
from functions.clear_screen import clear_screen
# função pra remover caracteres informados para cada coluna
def change_column_name(query):
    colunas = []
    j=0
    # iteração de correção inicial básica de nomes, definindo o padrão minúsculo e sem espaço
    # iteração faz a correção direto na tabela e adiciona nome na lista colunas para consulta constante do usuario
    print(f"Lista de colunas da tabela:\n")
    for column in query.columns:
        column = f'{column}'.lower().replace(" ","_")
        query.rename(columns={query.columns[j]:column},inplace=True)
        print(f"-{column}")
        colunas.append(column)
        j+=1

    print("\n")
    i=0
    # loop com condicionais que auxilia o usuário à realizar modificações manuais
    while True:
        # usuario utiliza guia da tabela colunas e decide se irá modificar algo manualemente
        # se não for ele só seguirá para a próxima etapa de ETL
        resposta = input("Deseja alterar algum/outro dos titulos listados?(s/n): ").lower()
        # confirmação do usuário
        if resposta == 's' or resposta=='n':
            if resposta == 'n':
                break
            else:
                # bloco de LookupError para escolha de qual nome deseja alterar
                while i<=0 or i>len(colunas):
                    try:
                        i=int(input(f"Informe qual a posição (1-{len(colunas)}), de baixo pra cima, do título que deseja alterar: "))
                    except ValueError:
                        print("Informe somente os números de posição")
                mudanca = input(f"Informe o nome novo de {colunas[i-1]} - ")
                # iteração da lista de colunas e de colunas na tabela para verificar existencia e correspondencia para substituição
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
                        print('\n')
                        break
                    else:
                        pass       
                i = 0
        else:
            print("Informe somente 's' ou 'n'\n")
        
    clear_screen()
    colunas = []
    return query