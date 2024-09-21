import banco_de_dados as bd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#1. Qual espécie de iris (Setosa, Versicolor, Virginica) tem a maior média de comprimento de pétala?
setosa = bd.setosa['PetalLengthCm']
versicolor = bd.versicolor['PetalLengthCm']
virginica = bd.virginica['PetalLengthCm']

def media(setosa,versicolor,virginica):
        setosa = setosa.mean()
        versicolor = versicolor.mean()
        virginica = virginica.mean()
        return f"Média de setosa: {setosa:.2f}CM", f"Média de versicolor: {versicolor:.2f}CM", f"Media de virginica: {virginica:.2f}CM"

print(media(setosa,versicolor,virginica))
#R: Maior media = Media de virginica: 5.55

#2. Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala?
"""
Usar grafico de dispersao

"""
sepala_setosaCM = bd.setosa['SepalLengthCm']
petala_setosaCM = bd.setosa['PetalLengthCm']

sepala_versicolorCM = bd.versicolor['SepalLengthCm']
petala_versicolorCM = bd.versicolor['PetalLengthCm']

sepala_virginicaCM = bd.virginica['SepalLengthCm']
petala_virginicaCM = bd.virginica['PetalLengthCm']


def criar_grafico_dispersao(sepala, petala):
    """
    Cria um gráfico de dispersão entre duas colunas do conjunto de dados. e coeficiente de parson
    """
    # Cria um DataFrame com os dados a serem plotados
    dados = pd.DataFrame({'SepalLengthCm': sepala, 'PetalLengthCm': petala})

    # Cria o gráfico de dispersão
    sns.scatterplot(data=dados, x='SepalLengthCm', y='PetalLengthCm', color='blue', label='Iris-setosa')

    # Configurações do gráfico
    plt.title('Gráfico de Dispersão: SepalLengthCm vs PetalLengthCm')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.show()
criar_grafico_dispersao(sepala_setosaCM, petala_setosaCM)
criar_grafico_dispersao(sepala_versicolorCM, petala_versicolorCM)
criar_grafico_dispersao(sepala_virginicaCM, petala_virginicaCM)

#3. Qual a distruibuição das espécies no banco de dados
"""
usar teste de normalidade + histograma
"""
#4. Quais caracteristicas (comprimento da sépala, largura da sépala, comprimento da pétala, largura de pétala) tem a maior variabilidade dentro de cada espécie?
