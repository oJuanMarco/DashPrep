# função pra trocar os caracteres por algum estabelecido e de padronização de células
from functions.clear_screen import clear_screen
# função de multipla escolha
import questionary

def char_change(query):
    # listas de caracteres que serão informados pelo usuário à serem substituidos na coluna
    lista_de_substituíveis = []
    lista_de_substitutos = []
    # entrada de iteração de colunas nas tabelas
    for column in query.columns:
        # view do usuário sobre qual coluna estamos e quais dados guarda
        print(f"\n{column} = {query[column].dtype}")
        print(f"Exemplo de dados: \n{query[column].iloc[1:6]}")
        # entrada de blocos for nas funções de troca automática dos meses e de troca manual
        i = 0
        j = 0
        # lista dos meses e de respectivos caracteres
        meses_ext = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
        meses_num = ['01','02','03','04','05','06','07','08','09','10','11','12']
        # condição que leva à iteração de meses utilizando as lista acima para fazer as trocas
        if 'data' in column:
            query[column] = query[column].str.replace("/","-")
            for j in range(len(meses_ext)):
                query[column] = query[column].str.replace(meses_ext[j],meses_num[j])
        # condição que verifica as entradas de valores para substituir as virgulas e tirar os pontos do milhar
        if query[column].astype(str).str.contains(',').any():
            query[column] = query[column].apply(lambda x: x.replace('.', '').replace(',', '.') if isinstance(x, str) and ',' in x else x)
        # loop de entrada para a altrações manuais
        while True:
            caractere_para_substituir = input("Informe o caractere que deseja substituir desta coluna (enter pra sair): ")
            # condicional onde se for substituir, continua, se não, sai do while true e vai pra proxima coluna da tabela
            if caractere_para_substituir == '':
                break
            else:
                # adiciona caractere que deseja tirar à lista e pede para informar por qual deseja tirar
                lista_de_substituíveis.append(caractere_para_substituir)
                caractere_substituto = input(f"Informe o caractere que deseja incluir desta coluna pelo '{lista_de_substituíveis[i]}': ")
                # nessa condicional/loop o programa não deixa sair enquanto o usuário não informa nada
                while True:
                    if caractere_substituto == '':
                        print("Informe um caractere válido, tente apertar espaço de quiser removêlo ;)\n")
                        break
                    else:
                        lista_de_substitutos.append(caractere_substituto)
                        # o usuário informa a troca, o programa responde sobre a decisão e adiciona os carateres nas listas
                        print(f"Caractere [{lista_de_substituíveis[i]}] trocado por [{lista_de_substitutos[i]}]")
                        break
        # programa itera listas e substitui os caracteres de mesma ordem pela coluna inteira
        for i in range(len(lista_de_substituíveis)):
            query[column] = query[column].str.replace(lista_de_substituíveis[i],lista_de_substitutos[i])
        # loop de decisão onde é possível alterar o padrão das strings para todas corresponderem aos mesmos algorismos (case sensitive)
        while True:
            # usuário informa por meio do terminal se deseja fazer essa alteração (se o padrão já estiver tratado não faz sentido entrar no loop)
            resposta = questionary.select('Deseja alterar o padrão de informações nos textos?',choices = ['não','sim']).ask()
            if resposta == 'não':
                break
            # se usuário informa não, sai e segue tratamento, caso contrário, entra e escolhe o padrão definido, também pelo terminal
            else:
                # a lib questionary e a função .select que faz a escolha
                resposta = questionary.select('Escolha a formatação desejada para as informações em texto: ',choices = ['Tudo maiúsculo','Tudo minúsculo','Iniciais maiúsculas']).ask()
                # match que dependendo da entrada escolhe qual será o comando para as linhas da coluna e então sai do loop
                match resposta:
                    case "Tudo maiúsculo":
                        query[column]=query[column].str.upper()
                        break
                    case "Tudo minúsculo":
                        query[column]=query[column].str.lower()
                        break
                    case _:
                        query[column]=query[column].str.title()
                        break
        # aqui limpa a tela e reseta lista para dar sequência à proxima coluna de maneira mais clara ao usuário e não dar conflito entre caracteres de colunas distintas
        clear_screen()
        lista_de_substituíveis = []
        lista_de_substitutos = []

    return query