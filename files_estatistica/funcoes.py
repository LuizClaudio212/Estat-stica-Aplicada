import numpy as np
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates

class Funcoes_Estatisticas:
    """
    Classe para realizar cálculos estatísticos e visualizações em dois conjuntos de dados.
    
    Atributos:
    dados1 (pd.Series): Dados para o primeiro conjunto.
    dados2 (pd.Series): Dados para o segundo conjunto.
    variancia_tipo (str): Tipo de variância a ser calculado, 'populacional' ou 'amostral'.
    """

    def __init__(self, dados1, dados2, variancia_tipo="populacional"):
        """
        Inicializa a classe com dois conjuntos de dados e o tipo de variância.

        Parâmetros:
        dados1 (pd.Series): Dados para o primeiro conjunto.
        dados2 (pd.Series): Dados para o segundo conjunto.
        variancia_tipo (str): Tipo de variância a ser calculado, 'populacional' ou 'amostral'.
        """
        self.dados1 = dados1
        self.dados2 = dados2
        if variancia_tipo not in ["populacional", "amostral"]:
            raise ValueError("O tipo de variância deve ser 'populacional' ou 'amostral'.")
        self.variancia_tipo = variancia_tipo

    def converter_data(self, coluna_data):
        """
        Converte uma coluna de data para o formato datetime.
        """
        self.dados1[coluna_data] = pd.to_datetime(self.dados1[coluna_data])
        #self.dados2[coluna_data] = pd.to_datetime(self.dados2[coluna_data])

    def criar_grafico_dispersao(self, x, y):
        """
        Cria um gráfico de dispersão entre duas colunas do conjunto de dados.
        """
        sns.scatterplot(data=self.dados1, x=x, y=y, label='Dados 1', color='blue')
        sns.scatterplot(data=self.dados2, x=x, y=y, label='Dados 2', color='orange')
        plt.title(f'Gráfico de Dispersão: {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend()
        plt.show()

    def criar_boxplot(self):
        """
        Plota boxplots para dois conjuntos de dados (dados1 e dados2).
        """
        plt.figure(figsize=(8, 6))
        plt.boxplot([self.dados1, self.dados2],
                    labels=['Dados 1', 'Dados 2'],
                    patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='blue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(markerfacecolor='red', marker='o'),
                    whiskerprops=dict(color='blue'))
        plt.title('Boxplot')
        plt.xlabel('Dados')
        plt.ylabel('Valor')
        plt.grid(True)
        plt.show()

    def criar_heatmap_correlacao(self, drop_columns=None):
        """
        Cria um heatmap de correlação entre as colunas do conjunto de dados.
        """
        if drop_columns:
            dados_corr = self.dados1.drop(columns=drop_columns)
        else:
            dados_corr = self.dados1
        
        corr_matrix = dados_corr.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Heatmap de Correlação')
        plt.show()

    def time_series(self):
        """
        Plota uma série temporal dos dados (assume que os dados possuem uma coluna 'Date').
        """
        if 'Date' in self.dados1.columns:
            sns.lineplot(data=self.dados1, x='Date', y='Low', label='Low - Dados 1')
            sns.lineplot(data=self.dados1, x='Date', y='High', label='High - Dados 1')
            #sns.lineplot(data=self.dados2, x='Date', y='Low', label='Low - Dados 2', color='orange')
            #sns.lineplot(data=self.dados2, x='Date', y='High', label='High - Dados 2', color='yellow')
            plt.legend()
            plt.title('Análise de Série Temporal')
            plt.xlabel('Data')
            plt.ylabel('Valor')
            plt.show()
        else:
            print("Erro: A coluna 'Date' não está presente nos dados.")

    # Funções estatísticas
    def media(self):
        x = self.dados1.mean()
        x2 = self.dados2.mean()
        return f"Média de dados1: {x}", f"Média de dados2: {x2}"

    def mediana(self):
        x = np.median(self.dados1)
        x2 = np.median(self.dados2)
        return f"Mediana de dados1: {x}", f"Mediana de dados2: {x2}"

    def percentil(self):
        primeiro_quartil_d1 = np.percentile(self.dados1, 25)
        terceiro_quartil_d1 = np.percentile(self.dados1, 75)
        
        primeiro_quartil_d2 = np.percentile(self.dados2, 25)
        terceiro_quartil_d2 = np.percentile(self.dados2, 75)
        return (f"Primeiro e terceiro quartil de dados1 = ({primeiro_quartil_d1}, {terceiro_quartil_d1})", 
                f"Primeiro e terceiro quartil de dados2 = ({primeiro_quartil_d2}, {terceiro_quartil_d2})")

    def variancia(self):
        ddof = 0 if self.variancia_tipo == 'populacional' else 1
        variancia_d1 = np.var(self.dados1, ddof=ddof)
        variancia_d2 = np.var(self.dados2, ddof=ddof)
        return (f"Variância de dados1 ({self.variancia_tipo}): {variancia_d1}", 
                f"Variância de dados2 ({self.variancia_tipo}): {variancia_d2}")

    def desviopadrao(self):
        ddof = 0 if self.variancia_tipo == 'populacional' else 1
        desviopadrao_d1 = np.std(self.dados1, ddof=ddof)
        desviopadrao_d2 = np.std(self.dados2, ddof=ddof)
        return (f"Desvio padrão de dados1 ({self.variancia_tipo}): {desviopadrao_d1}", 
                f"Desvio padrão de dados2 ({self.variancia_tipo}): {desviopadrao_d2}")

    def min_e_max(self):
        sub_d1 = max(self.dados1) - min(self.dados1)
        sub_d2 = max(self.dados2) - min(self.dados2)
        return (f"Minimo, máximo e subtração de dados1: min: {min(self.dados1)}, max: {max(self.dados1)}, sub: {sub_d1}",
                f"Minimo, máximo e subtração de dados2: min: {min(self.dados2)}, max: {max(self.dados2)}, sub: {sub_d2}")

    def intervalo_de_classes(self):
        """
        Plota histogramas dos dados1 e dados2.
        """
        plt.hist(self.dados1, bins=12, range=(12, 144), color='skyblue', edgecolor='black')
        plt.title("Histograma de dados1")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()
        
        plt.hist(self.dados2, bins=5, range=(65, 95), color='lightgreen', edgecolor='black')
        plt.title("Histograma de dados2")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()

    def outliers(self):
        """
        Identifica e retorna os outliers em dados1 e dados2.
        """
        mean_d1 = self.dados1.mean()
        std_d1 = self.dados1.std(ddof=1)
        ponto_corte_d1 = 3 * std_d1
        inf_d1, sup_d1 = mean_d1 - ponto_corte_d1, mean_d1 + ponto_corte_d1
        outliers_d1 = self.dados1[(self.dados1 < inf_d1) | (self.dados1 > sup_d1)]

        mean_d2 = self.dados2.mean()
        std_d2 = self.dados2.std(ddof=1)
        ponto_corte_d2 = 3 * std_d2
        inf_d2, sup_d2 = mean_d2 - ponto_corte_d2, mean_d2 + ponto_corte_d2
        outliers_d2 = self.dados2[(self.dados2 < inf_d2) | (self.dados2 > sup_d2)]

        return (f"Outliers de dados1: {outliers_d1.tolist()}", 
                f"Outliers de dados2: {outliers_d2.tolist()}")
