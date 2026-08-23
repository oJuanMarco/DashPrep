from functions.clear_screen import clear_screen

# função pra remover caracteres informados para cada coluna
def char_remove(query):
    # lista de elementos que serão indicados pelo usuário a remover
    lista_de_removiveis = []
    # iteração que passará por cada coluna da tabela para realizar as alterações nas linhas correspondentes
    for colunm in query.columns:
        # Indicação de coluna e 5 elementos de exemplo para melhor visualização do usuário
        print(f"\n{colunm} = {query[colunm].dtype}")
        print(f"Exemplo de dados: \n{query[colunm].iloc[1:6]}")
        print("\n")
        # loop em que o usuário adicionará os elementos que deseja remover à lista_de_removiveis, com saída caso não digite nada
        while True:
            caractere = input("Informe o caractere que deseja remover desta coluna (enter pra sair):")
            if caractere == '':
                break
            else:
                lista_de_removiveis.append(caractere)
        # loop de substituição+limpeza para melhor view+limpeza de lista para proximas colunas
        for i in range(len(lista_de_removiveis)):
            query[colunm] = query[colunm].str.replace(lista_de_removiveis[i],'')

        clear_screen()
        lista_de_removiveis = []
    return query