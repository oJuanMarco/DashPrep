def iteration(query):
    for colunm in query.columns:
        query[colunm] = query[colunm].str.strip().str.upper()
        print(query[colunm].iloc[:10])