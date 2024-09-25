import banco_de_dados as bd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro

#3. Qual a distruibuição das espécies no banco de dados

# Função para plotar histograma e realizar o teste de normalidade (Shapiro-Wilk)
def plot_histograma_e_normalidade(dados, coluna, especie):
    """
    Plota o histograma de uma coluna de dados para uma espécie e faz o teste de normalidade Shapiro-Wilk.
    """
    # Histograma
    sns.histplot(dados[coluna], kde=True, bins=10, color='blue', edgecolor='black')
    """
    a linha KDE é gerada com o parâmetro kde=True dentro da função sns.histplot. O Seaborn
    automaticamente adiciona essa curva suave ao histograma quando essa opção é ativada.
    dados[coluna]: Os dados da coluna (por exemplo, SepalLengthCm ou PetalLengthCm).
    color='blue': Define a cor das barras do histograma.
    edgecolor='black': Define a cor da borda das barras.
    """
    plt.title(f'Histograma de {coluna} ({especie})')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

    # Teste de normalidade Shapiro-Wilk
    stat, p_value = shapiro(dados[coluna])
    print(f'Teste de normalidade Shapiro-Wilk para {coluna} ({especie}):')
    print(f'Estatística={stat:.4f}, p-valor={p_value:.4f}')
    print('-' * 50)


# Executando o código para as três espécies (setosa, versicolor, virginica)
for especie, df_especie in zip(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], 
                               [bd.setosa, bd.versicolor, bd.virginica]):
    print(f'\n### {especie} ###')
    plot_histograma_e_normalidade(df_especie, 'SepalLengthCm', especie)
    plot_histograma_e_normalidade(df_especie, 'PetalLengthCm', especie)
