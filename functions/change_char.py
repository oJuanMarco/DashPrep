# função pra trocar os caracteres por algum estabelecido e de padronização de células
from functions.clear_screen import clear_screen
from pick import pick

def char_remove(query):
    lista_de_substituíveis = []
    lista_de_substitutos = []

    for colunm in query.columns:
        print(f"\n{colunm} = {query[colunm].dtype}")
        print(f"Exemplo de dados: \n{query[colunm].iloc[1:6]}")
        print("\n")

        i = 0

        while True:
            caractere_para_substituir = input("Informe o caractere que deseja substituir desta coluna (enter pra sair):")
            if caractere == '':
                break
            else:
                lista_de_substituíveis.append(caractere_para_substituir)
                caractere_substituto = input(f"Informe o caractere que deseja incluir desta coluna pelo {lista_de_substituíveis[i]}: ")
                while True:
                    if caractere == '':
                        print("Informe um caractere válido, tente apertar espaço de quiser removêlo ;)\n")
                    else:
                        lista_de_substitutos.append(caractere_substituto)
                        print(f"Caractere [{lista_de_substituíveis[i]}] trocado por [{lista_de_substitutos[i]}]")
                        break
                        
        for i in range(len(lista_de_substituíveis)):
            query[colunm] = query[colunm].str.replace(lista_de_substituíveis[i],lista_de_substitutos[i])

        while True:
            resposta = input("Deseja alterar o padrão de informações nos textos? (s/n): ")
            if resposta == 's' or resposta=='n':
                if resposta == 'n':
                    break
                else:
                    resposta = pick(['Tudo maiúsculo','Tudo minúsculo','Iniciais maiúsculas'],'Escolha a formatação desejada para as informações em texto: ')
                    match resposta:
                        case "Tudo maiúsculo":
                            query[colunm]=query[colunm].str.upper()
                        case "Tudo minúsculo":
                            query[colunm]=query[colunm].str.lower()
                        case _:
                            query[colunm]=query[colunm].str.title()
            else:
                print("Informe somente 's' ou 'n'\n")


        clear_screen()
        lista_de_substituíveis = []
        lista_de_substitutos = []

    return query