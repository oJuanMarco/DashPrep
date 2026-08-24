# função que remove linha se tiver dado vazio ou periodo de transações > 12
# adiciona contador pra analizar quantas linhas foram removidas

def row_remove(query):
    
    soma = query.isna().any(axis=1).sum()
        
    print(f"{soma} linhas deletadas de {len(query)} linhas")
    input(f"Cera de {(soma/len(query))*100:.2f}%")