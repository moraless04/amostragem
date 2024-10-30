import pandas as pd

df = pd.read_csv('alugueis.csv')

df_amostra_aleatoria = amostragem_aleatoria(df, 100)

df_amostra_estratificada = amostragem_estratificada(df, 200, 'city')

def discretizar_area(area):
    if area <= 50:
        return 'PEQUENO'
    elif area <= 100:
        return 'MÉDIO'
    else:
        return 'GRANDE'

df['area_categoria'] = df['area'].apply(discretizar_area)

df['total_categoria'] = pd.qcut(df['total'], 5, labels=False)

df_one_hot_encoded = pd.get_dummies(df, columns=['total_categoria'])

print("Amostragem Aleatória (100 amostras):")
print(df_amostra_aleatoria.head())

print("\nAmostragem Estratificada (200 amostras):")
print(df_amostra_estratificada.head())

print("\nDataset com área discretizada:")
print(df[['area', 'area_categoria']].head())

print("\nDataset com total discretizado e one-hot encoded:")
print(df_one_hot_encoded.head())