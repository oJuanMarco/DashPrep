# import do pandas para manipulação de dados, da função e variaveis pro funcionamento do código
import pandas as pd
from functions.read import read_file
from functions.treatment import treatment
from variables.tables import clientes, contas, emprestimos, transacoes

# lista com tabelas para identação no for e variavel para localizar qual a tabela referente
tabelas = [clientes,contas,emprestimos,transacoes]
var = 0

# laço passa por cada tabela da lista
for tabela in tabelas:
    # printa de qual tabela os dados correspondem
    print(f"Dados da tabela {str(tabelas[var]).capitalize()}:")
    # leitura dos dados da tabela pelo pandas
    dados = read_file(tabela)
    # função principal para o tratamento correto dos dados
    treatment(dados)
    # soma de variavel pra passagem da proxima tabela
    var+=1