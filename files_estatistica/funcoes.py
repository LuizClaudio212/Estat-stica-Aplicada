import numpy as np
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates

class Funcoes_Estatisticas:
    """
    Classe para realizar cálculos estatísticos em dois conjuntos de dados.

    Atributos:
    dados1 (pd.Series): Dados para o primeiro conjunto.
    dados2 (pd.Series): Dados para o segundo conjunto.
    variancia_tipo (str): Tipo de variância a ser calculado, 'populacional' ou 'amostral'.

    Métodos:
    media: Calcula a média dos dados.
    mediana: Calcula a mediana dos dados.
    percentil: Calcula o primeiro e o terceiro quartil dos dados.
    moda: Calcula a moda dos dados.
    amplitude: Calcula a amplitude dos dados.
    amplitude_interquartil: Calcula a amplitude interquartil dos dados.
    variancia: Calcula a variância dos dados.
    desviopadrao: Calcula o desvio padrão dos dados.
    min_e_max: Calcula o mínimo, máximo e a subtração entre eles dos dados.
    intervalo_de_classes: Plota o histograma dos dados com intervalos de classes.
    outliers: Identifica e retorna os outliers nos dados.
    boxplot:  Plota boxplots para dois conjuntos de dados (dados1 e dados2).
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
    
    def media(self):
        """
        Calcula a média dos dois conjuntos de dados.

        Retorna:
        tupla: Média de dados1 e dados2.
        """
        x = self.dados1.mean()
        x2 = self.dados2.mean()
        return f"Média de dados1: {x}", f"Média de dados2: {x2}"
    
    def mediana(self):
        """
        Calcula a mediana dos dois conjuntos de dados.

        Retorna:
        tupla: Mediana de dados1 e dados2.
        """
        x = np.median(self.dados1)
        x2 = np.median(self.dados2)
        return f"Mediana de dados1: {x}", f"Mediana de dados2: {x2}"
        
    def percentil(self):
        """
        Calcula o primeiro e o terceiro quartil dos dois conjuntos de dados.

        Retorna:
        tupla: Primeiro e terceiro quartil de dados1 e dados2.
        """
        primeiro_quartil_d1 = np.percentile(self.dados1, 25)
        terceiro_quartil_d1 = np.percentile(self.dados1, 75)
        
        primeiro_quartil_d2 = np.percentile(self.dados2, 25)
        terceiro_quartil_d2 = np.percentile(self.dados2, 75)
        return (f"Primeiro e terceiro quartil de dados1 = ({primeiro_quartil_d1}, {terceiro_quartil_d1})", 
                f"Primeiro e terceiro quartil de dados2 = ({primeiro_quartil_d2}, {terceiro_quartil_d2})")
    
    def moda(self):
        """
        Calcula a moda dos dois conjuntos de dados.

        Retorna:
        tupla: Moda de dados1 e dados2.
        """
        x = sta.multimode(self.dados1)
        x2 = sta.multimode(self.dados2)
        return f"Moda de dados1: {x}", f"Moda de dados2: {x2}"
    
    def amplitude(self):
        """
        Calcula a amplitude dos dois conjuntos de dados.

        Retorna:
        tupla: Amplitude de dados1 e dados2.
        """
        x = np.ptp(self.dados1)
        x2 = np.ptp(self.dados2)
        return f"Amplitude de dados1: {x}", f"Amplitude de dados2: {x2}"
    
    def amplitude_interquartil(self):
        """
        Calcula a amplitude interquartil dos dois conjuntos de dados.

        Retorna:
        tupla: Amplitude interquartil (IQR) de dados1 e dados2.
        """
        q1_d1 = np.percentile(self.dados1, 25)
        q3_d1 = np.percentile(self.dados1, 75)
        iqr1 = q3_d1 - q1_d1
        
        q1_d2 = np.percentile(self.dados2, 25)
        q3_d2 = np.percentile(self.dados2, 75)        
        iqr2 = q3_d2 - q1_d2
        return f"IQR de dados1: {iqr1}", f"IQR de dados2: {iqr2}"
    
    def variancia(self):
        """
        Calcula a variância dos dois conjuntos de dados.

        Retorna:
        tupla: Variância de dados1 e dados2, com base no tipo especificado.
        """
        ddof = 0 if self.variancia_tipo == 'populacional' else 1
        variancia_d1 = np.var(self.dados1, ddof=ddof)
        variancia_d2 = np.var(self.dados2, ddof=ddof)
        return (f"Variância de dados1 ({self.variancia_tipo}): {variancia_d1}", 
                f"Variância de dados2 ({self.variancia_tipo}): {variancia_d2}")
    
    def desviopadrao(self):
        """
        Calcula o desvio padrão dos dois conjuntos de dados.

        Retorna:
        tupla: Desvio padrão de dados1 e dados2, com base no tipo especificado.
        """
        ddof = 0 if self.variancia_tipo == 'populacional' else 1
        desviopadrao_d1 = np.std(self.dados1, ddof=ddof)
        desviopadrao_d2 = np.std(self.dados2, ddof=ddof)
        return (f"Desvio padrão de dados1 ({self.variancia_tipo}): {desviopadrao_d1}", 
                f"Desvio padrão de dados2 ({self.variancia_tipo}): {desviopadrao_d2}")

    def min_e_max(self):
        """
        Calcula o mínimo, máximo e a subtração entre os valores mínimo e máximo dos dois conjuntos de dados.

        Retorna:
        tupla: Mínimo, máximo e subtração entre mínimo e máximo para dados1 e dados2.
        """
        sub_d1 = max(self.dados1) - min(self.dados1)
        sub_d2 = max(self.dados2) - min(self.dados2)
        return (f"minimo, maximo e subtracao de dados1: min: {min(self.dados1)}, max: {max(self.dados1)}, sub: {sub_d1}",
                f"minimo, maximo e subtracao de dados2: min: {min(self.dados2)}, max: {max(self.dados2)}, sub: {sub_d2}")
                
    def intervalo_de_classes(self):
        """
        Plota histogramas dos dados1 e dados2 com intervalos de classes especificados.

        Observação:
        - Para dados1, um histograma é exibido.
        - Para dados2, outro histograma é exibido.
        """
        plt.hist(self.dados1, bins=12, range=(12, 144))
        plt.title("Histograma de dados1")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()
        
        plt.hist(self.dados2, bins=5, range=(65, 95))
        plt.title("Histograma de dados2")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()
               
    def outliers(self):
        """
        Identifica outliers nos dois conjuntos de dados com base no método do desvio padrão.

        Retorna:
        tupla: Outliers de dados1 e dados2 como listas.
        """
        # Identificação de outliers para dados1
        mean_d1 = self.dados1.mean()
        std_d1 = self.dados1.std(ddof=1)  # Usando ddof=1 para amostral
        ponto_corte_d1 = 3 * std_d1
        inf_d1, sup_d1 = mean_d1 - ponto_corte_d1, mean_d1 + ponto_corte_d1
        outliers_d1 = self.dados1[(self.dados1 < inf_d1) | (self.dados1 > sup_d1)]

        # Identificação de outliers para dados2
        mean_d2 = self.dados2.mean()
        std_d2 = self.dados2.std(ddof=1)  # Usando ddof=1 para amostral
        ponto_corte_d2 = 3 * std_d2
        inf_d2, sup_d2 = mean_d2 - ponto_corte_d2, mean_d2 + ponto_corte_d2
        outliers_d2 = self.dados2[(self.dados2 < inf_d2) | (self.dados2 > sup_d2)]

        return (f"Outliers de dados1: {outliers_d1.tolist()}", 
                f"Outliers de dados2: {outliers_d2.tolist()}")

    def boxplot(self):
        """
        Plota boxplots para dois conjuntos de dados (dados1 e dados2).

        Esta função cria um boxplot para cada conjunto de dados, mostrando a distribuição, 
        a dispersão, o desvio da simetria e os outliers.

        Parâmetros:
        dados1 (array-like): Primeiro conjunto de dados a ser plotado.
        dados2 (array-like): Segundo conjunto de dados a ser plotado.
        """
        
        # Cria uma figura e eixos para os subplots
        plt.figure(figsize=(12, 6))
        
        # Plota boxplot para dados1
        plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, posição 1
        sns.boxplot(data=self.dados1)
        plt.title('Boxplot de dados1')
        plt.xlabel('Dados1')
        
        # Plota boxplot para dados2
        plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, posição 2
        sns.boxplot(data=self.dados2)
        plt.title('Boxplot de dados2')
        plt.xlabel('Dados2')
        
        # Ajusta o layout e exibe os plots
        plt.tight_layout()
        plt.show()

    def time_series(self):
        sns.lineplot(data=self.dados1, x='Date',y='Open')
        plt.show()