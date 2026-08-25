# import do pandas para manipulação de dados, da função e variaveis pro funcionamento do código
import pandas as pd
from functions.read import read_file
from functions.treatment import treatment
from variables.tables import clientes, contas, emprestimos, transacoes

# lista com tabelas para iteração no for e variavel para localizar qual a tabela referente
tabelas = [clientes,contas,emprestimos,transacoes]

var = 0
try:
    # laço passa por cada tabela da lista
    for tabela in tabelas:
        # printa de qual tabela os dados correspondem
        print(f"Dados da tabela {str(tabelas[var]).capitalize()}:")
        # leitura dos dados da tabela pelo pandas
        dados = read_file(tabela)
        # função principal para o tratamento correto dos dados
        tratamento = treatment(dados)
        # exporta cópia de tabela tratada
        tratamento.to_csv(f"{tabela}_tratado.csv",index=False)
        # avisa usuário sobre conclusão do processo
        input(f"{tabela} exportada com sucesso!")

        var+=1
except Exception as e:
    print(f"Erro: {e}")