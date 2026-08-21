from functions.clear_screen import clear_screen

# função pra remover caracteres informados para cada coluna
def char_remove(query):

    lista_de_removiveis = []
    for colunm in query.columns:

        print(f"\n{colunm} = {query[colunm].dtype}")
        print(f"Exemplo de dado: \n{query[colunm].iloc[1:6]}")
        print("\n")

        while True:
            caractere = input("Informe o caractere que deseja remover desta coluna (enter pra sair):")
            if caractere == '':
                break
            else:
                lista_de_removiveis.append(caractere)
        
        for i in range(len(lista_de_removiveis)):
            query[colunm] = query[colunm].str.replace(lista_de_removiveis[i],'')

        clear_screen()
        lista_de_removiveis = []
    return query