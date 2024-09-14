import matplotlib.dates as mdates
import banco_de_dados as bd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
from funcoes import Funcoes_Estatisticas


#dados1 = bd.iris['PetalLengthCm']
#dados2 = bd.iris['PetalWidthCm']

#estatistica = Funcoes_Estatisticas(dados1, dados2, variancia_tipo='populacional')
#inverter o formato da data
#bd.stock['Date'] = pd.to_datetime(bd.stock['Date'])
x = bd.iris['PetalLengthCm']
y = bd.iris['PetalWidthCm']


#mostrar informações dos dados
#print(bd.stock.head())
#print(bd.iris.head())



#Analise de variabilidade de determinado dado em função do tempo
#dados1 = bd.stock
def time_series(dados1):
    sns.lineplot(dados1, x='Date',y='High')
    sns.lineplot(dados1, x='Date', y='Low')
    plt.show()

#Grafico de dispersão
"""
Representa a relação entre duas variaveis.

"""

def grafico_de_dispersao(dados1,x,y):

    sns.scatterplot(dados1,x=x, y=y)
    plt.show()




def boxplot(x,y):
    x = x
    y = y
    plt.boxplot([x,y])
    plt.show()
#print(time_series(dados1))

#grafico_de_dispersao(dados1,x,y)

#print(boxplot(x,y))

iris_setosa = bd.iris[bd.iris['Species'] == 'Iris-setosa']
iris_versicolor = bd.iris[bd.iris['Species'] == 'versicolor']
iris_virginica = bd.iris[bd.iris['Species'] == 'virginica']

x = bd.iris['SepalLengthCm']
y = bd.iris['SepalWidthCm']
x1 = bd.iris['SepalLengthCm']
y1 = bd.iris['PetalWidthCm']
"""
sns.scatterplot(data = iris_setosa, x=x, y=y)
plt.show()
sns.scatterplot(data = iris_setosa, x=x, y=y1)
plt.show()
sns.scatterplot(data = iris_setosa, x=x1, y=y)
plt.show()
"""
drop = iris_setosa.drop(columns=['Id', 'Species'])
corrmatrix = drop.corr()
print(corrmatrix)

sns.heatmap(corrmatrix, annot=True)
plt.show()
#print(iris_setosa.head())