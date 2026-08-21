# função que tem 2 funcionalidades: 
# -tirar o espaço em branco das linhas e cabeçalhos
# -converter tudo para string para leitura dos proximos passos
def blank_space_remove(query):
    # tira espaço em branco dos cabeçalhos
    query.columns = query.columns.str.strip()
    for colunm in query.columns:
        if query[colunm].dtype == 'str':
            # tira branco das linhas
            query[colunm] = query[colunm].str.strip()
        else:
            # converte pra string e tira branco das linhas  
            query[colunm] = query[colunm].astype(str).str.strip()
    return query