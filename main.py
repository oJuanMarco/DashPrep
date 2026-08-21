# import do pandas para manipulação de dados, da função e variaveis pro funcionamento do código
import pandas as pd
from read import read_file
from tables import clientes, contas, emprestimos, transacoes

tabela1 = read_file(clientes)
tabela2 = read_file(contas)
tabela3 = read_file(emprestimos)
tabela4 = read_file(transacoes)

# print(tabela1+"oi") == Se eu somar a leitura à um elemento, todos os elementos da tabela
# serão afetados
for colunm in tabela1.columns:
    print(colunm)