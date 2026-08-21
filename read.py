# import da biblioteca
import pandas as pd

# função base de leitura e conversão do encoding dos aruivos importados
def read_file(file_path):
    # o "sep" como x or y não era reconhecido na pretica, então foi necessário 
    # criar um try/except para tentar ler o arquivo com os dois separadores possíveis
    try:
        # leitura de aruivos no padrão UTF-8 retornarão seu padrão em colunas dividas por ';' ou ','
        try:
            return pd.read_csv(file_path, encoding='utf-8', sep=',', index_col=False)
        except pd.errors.ParserError:
            return pd.read_csv(file_path, encoding='utf-8', sep=';', index_col=False)
    except UnicodeDecodeError:
        # leitura de aruivos no padrão UTF-16 retornarão em latin-1 em colunas dividas por ';' ou ','
        # para leitura dos arquivos não serem afetadas por caracteres desconhecidos
        try:
            return pd.read_csv(file_path, encoding='latin-1', sep=';', index_col=False)
        except pd.errors.ParserError:
            return pd.read_csv(file_path, encoding='latin-1', sep=',', index_col=False)