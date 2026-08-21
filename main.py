# import do pandas para manipulação de dados, da função e variaveis pro funcionamento do código
import pandas as pd
from read import read_file
from tables import clientes, contas, emprestimos, transacoes

tabelas = [clientes,contas,emprestimos,transacoes]

# print(tabela1+"oi") == Se eu somar a leitura à um elemento, todos os elementos da tabela
# serão afetados
var = 0
for tabela in tabelas:
    print(f"Dados da tabela {str(tabelas[var]).capitalize()}:")
    dados = read_file(tabela)
    for colunm in dados.columns:
        # print(dados[colunm].head(1))
        print(f"{colunm} = {dados[colunm].dtype}")
        print(f"Exemplo de dado: {dados[colunm].iloc[0]}")
    print("\n")
    var+=1