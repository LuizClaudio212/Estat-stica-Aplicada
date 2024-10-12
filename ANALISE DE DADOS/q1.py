"""
Um pesquisador está estudando a eficacia de dois metodos de ensino diferentes nas notas dos alunos. O primeiro grupo A ultiliza o metodos 1, e o segundo grupo (Grupo B) utiliza o mnetodos 2:
realize um teste de hipoteses (com nivel de confiança de 0,05)
 e forneça uma conclusão sobre a media da população de dados"""

import numpy as np
import statistics
from scipy.stats import shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as  plt
import scikit_posthocs as sp

grupo_a = np.array([80,85,90,78,82,88,84])
grupo_b = np.array([78,80,85,88,82,86,90])

#desvio padrão e amplitude para grupo A
print(np.std(grupo_a))
print(np.ptp(grupo_a))

#desvio padrão e amplitude para grupo B
print(np.std(grupo_b))
print(np.ptp(grupo_b))

#media dos dois grupos
print(grupo_a.mean())
print(grupo_b.mean())

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


check_normality(grupo_a)#p value 0.9560
check_normality(grupo_b)#p value 0.9026

#os dois possuem distribuição normal



ttest,p_value = stats.ttest_ind(grupo_a,grupo_b)
print("p value:%.8f" % p_value)
print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
if p_value/2 <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


posthoc_df= sp.posthoc_ttest([grupo_a,grupo_b], equal_var=True, p_adjust="bonferroni")

group_names= ["Grupo A", "Grupo B"]
posthoc_df.columns= group_names
posthoc_df.index= group_names
posthoc_df.style.applymap(lambda x: "background-color:violet" if x<0.05 else "background-color: white")


print(grupo_a.mean())
print(grupo_b.mean())


"""
sns.distplot(grupo_a)
plt.show()


sns.distplot(grupo_b)
plt.show()
"""

"""
Relatório sobre a Eficácia dos Métodos de Ensino
Introdução Este estudo avalia a eficácia de dois métodos de ensino diferentes nos resultados dos alunos. O Grupo A utilizou o Método 1, enquanto o Grupo B utilizou o Método 2. O objetivo é determinar se há uma diferença significativa nas médias das notas dos alunos entre os dois grupos, utilizando um nível de confiança de 0,05.

Análise Descritiva

Grupo A: 

Média: 83,86

Desvio Padrão: 3,85

Amplitude: 12

Grupo B:

Média: 84,14

Desvio Padrão: 4,23

Amplitude: 12

Teste de Normalidade O teste Shapiro-Wilk foi aplicado para verificar a normalidade dos dados:

p-valor para Grupo A: 0,9560 (dados normalmente distribuídos)

p-valor para Grupo B: 0,9026 (dados normalmente distribuídos)

Teste de Hipóteses O teste t independente foi realizado para comparar as médias dos dois grupos:

p-valor: 0,4828

Considerando que a hipótese é unidirecional, o p-valor ajustado é 0,2414

Como o p-valor ajustado é maior que 0,05, não rejeitamos a hipótese nula.

Conclusão Com base nos testes realizados, não há diferença estatisticamente significativa entre as médias dos métodos de ensino utilizados pelos Grupos A e B. Ambos os métodos apresentam eficácia similar nas notas dos alunos.


"""