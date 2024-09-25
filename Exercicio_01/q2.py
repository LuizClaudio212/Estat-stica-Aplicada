import banco_de_dados as bd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro, pearsonr, spearmanr

# 2. Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala?
"""
Usar gráfico de dispersão e teste de normalidade (Shapiro-Wilk)
"""
sepala_setosaCM = bd.setosa['SepalLengthCm']
petala_setosaCM = bd.setosa['PetalLengthCm']

sepala_versicolorCM = bd.versicolor['SepalLengthCm']
petala_versicolorCM = bd.versicolor['PetalLengthCm']

sepala_virginicaCM = bd.virginica['SepalLengthCm']
petala_virginicaCM = bd.virginica['PetalLengthCm']


def criar_grafico_dispersao_e_corr(sepala, petala, especie):
    """
    Cria um gráfico de dispersão entre duas colunas do conjunto de dados,
    faz o teste de normalidade e calcula a correlação apropriada.
    """
    # Cria um DataFrame com os dados a serem plotados
    dados = pd.DataFrame({'SepalLengthCm': sepala, 'PetalLengthCm': petala})

    # Cria o gráfico de dispersão
    sns.scatterplot(data=dados, x='SepalLengthCm', y='PetalLengthCm', label=especie)

    # Configurações do gráfico
    plt.title(f'Gráfico de Dispersão: SepalLengthCm vs PetalLengthCm ({especie})')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.show()

    # Teste de normalidade (Shapiro-Wilk)
    stat_sepala, p_sepala = shapiro(sepala)
    stat_petala, p_petala = shapiro(petala)

    print(f'Teste de normalidade Shapiro-Wilk para {especie}:')
    print(f'  SepalLengthCm: estatística={stat_sepala:.4f}, p-valor={p_sepala:.4f}')
    print(f'  PetalLengthCm: estatística={stat_petala:.4f}, p-valor={p_petala:.4f}')

    # Verifica se ambos os dados são normalmente distribuídos
    if p_sepala > 0.05 and p_petala > 0.05:
        # Usar correlação de Pearson
        coef, p_value = pearsonr(sepala, petala)
        print(f'Correlação de Pearson para {especie}: coeficiente={coef:.4f}, p-valor={p_value:.4f}')
    else:
        # Usar correlação de Spearman
        coef, p_value = spearmanr(sepala, petala)
        print(f'Correlação de Spearman para {especie}: coeficiente={coef:.4f}, p-valor={p_value:.4f}')


# Chamadas para criar gráficos, executar o teste de normalidade e calcular a correlação
criar_grafico_dispersao_e_corr(sepala_setosaCM, petala_setosaCM, 'Iris-setosa')
criar_grafico_dispersao_e_corr(sepala_versicolorCM, petala_versicolorCM, 'Iris-versicolor')
criar_grafico_dispersao_e_corr(sepala_virginicaCM, petala_virginicaCM, 'Iris-virginica')
