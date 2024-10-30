import pandas as pd

def amostragem_aleatória(dataframe, amostras, reposicao=True):
    """
    Realiza uma amostragem aleatória de um dataframe.

    Parâmetros:
    dataframe (pd.DataFrame): O dataframe contendo os dados.
    amostras (int): O número de amostras desejadas.
    reposicao (bool): Se a amostragem deve ser feita com reposição (default é True).

    Retorna:
    pd.DataFrame: Um dataframe com o número exato de amostras.
    """
    return dataframe.sample(n=amostras, replace=reposicao)