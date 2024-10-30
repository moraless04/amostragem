import pandas as pd

def amostragem_estratificada(dataframe, amostras, coluna):
    """
    Realiza uma amostragem estratificada de um dataframe.

    Parâmetros:
    dataframe (pd.DataFrame): O dataframe contendo os dados.
    amostras (int): O número de amostras desejadas.
    coluna (str): O nome da coluna para estratificação.

    Retorna:
    pd.DataFrame: Um dataframe com o número exato de amostras, mantendo a proporção de valores da coluna escolhida.
    """
    # Calcula a proporção de cada valor na coluna
    proporcoes = dataframe[coluna].value_counts(normalize=True)
    
    # Calcula o número de amostras para cada valor na coluna
    amostras_por_valor = (proporcoes * amostras).round().astype(int)
    
    # Realiza a amostragem estratificada
    amostras_estratificadas = [dataframe[dataframe[coluna] == valor].sample(n=n, replace=True) 
                               for valor, n in amostras_por_valor.items()]
    
    # Concatena as amostras em um único dataframe
    resultado = pd.concat(amostras_estratificadas)
    
    return resultado