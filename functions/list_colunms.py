def list_colunms(query):
    for colunm in query.columns:
        print(f"{colunm} = {query[colunm].dtype}")
        print(f"Exemplo de dado: {query[colunm].iloc[0]}")
    print("\n")