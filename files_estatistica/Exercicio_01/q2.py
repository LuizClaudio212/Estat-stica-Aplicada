import banco_de_dados as bd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro

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


def criar_grafico_dispersao(sepala, petala, especie):
    """
    Cria um gráfico de dispersão entre duas colunas do conjunto de dados e faz o teste de normalidade.
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

    # Teste de normalidade Shapiro-Wilk
    stat_sepala, p_sepala = shapiro(sepala)
    stat_petala, p_petala = shapiro(petala)
    
    print(f'Teste de Shapiro-Wilk para SepalLengthCm ({especie}): Stat={stat_sepala:.3f}, p-valor={p_sepala:.3f}')
    print(f'Teste de Shapiro-Wilk para PetalLengthCm ({especie}): Stat={stat_petala:.3f}, p-valor={p_petala:.3f}')
    
    # Interpretação do resultado
    if p_sepala > 0.05:
        print(f'SepalLengthCm ({especie}) parece seguir uma distribuição normal.')
    else:
        print(f'SepalLengthCm ({especie}) não segue uma distribuição normal.')
    
    if p_petala > 0.05:
        print(f'PetalLengthCm ({especie}) parece seguir uma distribuição normal.')
    else:
        print(f'PetalLengthCm ({especie}) não segue uma distribuição normal.')


# Chamadas para criar gráficos e executar o teste de normalidade
criar_grafico_dispersao(sepala_setosaCM, petala_setosaCM, 'Iris-setosa')
criar_grafico_dispersao(sepala_versicolorCM, petala_versicolorCM, 'Iris-versicolor')
criar_grafico_dispersao(sepala_virginicaCM, petala_virginicaCM, 'Iris-virginica')
