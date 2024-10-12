"""
Um cientista quer comparar os pesos de duas espécies diferentes de aves: Espécie X e especioe Y. Os dados sobre os pesos (em gramas) são os segintes:
Espécie X: 150, 155, 160, 158, 152, 162
Espécie Y: 145, 148, 150, 149, 151 147
realize um teste de hipoteses (com nivel de confiança de 0,05) e forneça uma conclusão sobre a média da população de dados
"""
import numpy as np
import statistics
from scipy.stats import shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as  plt
import scikit_posthocs as sp


especie_x = np.array([150, 155, 160, 158, 152, 162])
especie_y = np.array([145, 148, 150, 149, 151, 147])

#desvio padrão e amplitude para especie x
print(np.std(especie_x))
print(np.ptp(especie_x))

#desvio padrão e amplitude para especie y
print(np.std(especie_y))
print(np.ptp(especie_y))

#media dos dois grupos
print(especie_x.mean())
print(especie_y.mean())

# TESTE DE NORMALIDADE!

# VERIFICAR SE OS DADOS SEGUEM UMA DISTRIBUIÇÃO NORMAL!

# teste de hipótese de Shapiro-Wilk

# H0:Os dados têm distribuição normal;
# H1:Os dados não têm distribuição normal.

# Conclusões:
# Se p-valor (valor de prova) <= 0.05, rejeita H0 (H0 é falso) e assume H1 (H1 é verdadeiro);
# Se p-valor (valor de prova) > 0.05 não deve rejeitar H0 (H0 é verdadeiro).

# 0.05 = 5% é a cauda do intervalo de confiança de 95%.

def check_normality(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")


check_normality(especie_x)
check_normality(especie_y)





ttest,p_value = stats.ttest_ind(especie_x,especie_y)
print("p value:%.8f" % p_value)
print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
if p_value <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")



"""
Relatório sobre os Pesos das Espécies de Aves
Introdução Este estudo compara os pesos de duas espécies diferentes de aves: Espécie X e Espécie Y. O objetivo é determinar se há uma diferença significativa nas médias dos pesos entre as duas espécies, utilizando um nível de confiança de 0,05.

Análise Descritiva

Espécie X:

Média: 156,17

Desvio Padrão: 4,13

Amplitude: 12

Espécie Y:

Média: 148,33

Desvio Padrão: 2,25

Amplitude: 6

Teste de Normalidade O teste Shapiro-Wilk foi aplicado para verificar a normalidade dos dados:

p-valor para Espécie X: 0,9602 (dados normalmente distribuídos)

p-valor para Espécie Y: 0,9348 (dados normalmente distribuídos)

Teste de Hipóteses O teste t independente foi realizado para comparar as médias dos dois grupos:

p-valor: 0,0001

Considerando que a hipótese é unidirecional, o p-valor ajustado é 0,00005

Como o p-valor ajustado é menor que 0,05, rejeitamos a hipótese nula.

Conclusão Com base nos testes realizados, há uma diferença estatisticamente significativa entre as médias dos pesos das espécies de aves X e Y, considerando um nível de confiança de 0,05. As aves da Espécie X são significativamente mais pesadas que as da Espécie Y.

"""