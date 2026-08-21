def blank_space_remove(query):
    for colunm in query.columns:
        if query[colunm].dtype == 'str':
            query[colunm] = query[colunm].str.strip()
            print(query[colunm].iloc[:10])
        else:
            query[colunm] = query[colunm].astype(str).str.strip()
            print(query[colunm].iloc[:10])