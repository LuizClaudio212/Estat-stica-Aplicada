import banco_de_dados as bd
import pandas as pd


#4. Quais caracteristicas (comprimento da sépala, largura da sépala, comprimento da pétala, largura de pétala) tem a maior variabilidade dentro de cada espécie?

# Função para calcular a variabilidade (desvio padrão) de cada característica
def calcular_variabilidade_por_especie(df, especie):
    """
    Calcula a variabilidade (desvio padrão e variância) de cada característica para a espécie.
    """
    variabilidade = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].std()
    variancia = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].var()

    print(f"\n### {especie} ###")
    print(f"Desvio Padrão:\n{variabilidade}")
    print(f"\nVariância:\n{variancia}")
    print('-' * 50)

    # Identificar a característica com maior variabilidade
    maior_variabilidade = variabilidade.idxmax()
    maior_variancia = variancia.idxmax()

    print(f"Característica com maior variabilidade (Desvio Padrão): {maior_variabilidade}")
    print(f"Característica com maior variabilidade (Variância): {maior_variancia}")
    print('=' * 50)


# Executar para cada espécie (Iris-setosa, Iris-versicolor, Iris-virginica)
calcular_variabilidade_por_especie(bd.setosa, 'Iris-setosa')
calcular_variabilidade_por_especie(bd.versicolor, 'Iris-versicolor')
calcular_variabilidade_por_especie(bd.virginica, 'Iris-virginica')
