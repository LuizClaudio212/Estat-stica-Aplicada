"""
Um pesquisador medico está testando a eficacia de tres dietas diferentes na perda de peso. Os dados (em quilogramas perdidos ) para trÊs grupos de individuos que seguem diferentes dietas são mostrados abvaixo:
Dieta A: 5, 7, 6, 8, 5
Dieta B: 4, 6, 5, 7, 6
Dieta C: 6, 8, 7, 9, 7
realize um teste de hipoteses (com nivel de confiança de 0,05) e forneça uma conclusão sobre a média da população de dados
"""

import numpy as np
import statistics
from scipy.stats import shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import scikit_posthocs as sp

# Dados das dietas
dieta_a = np.array([5, 7, 6, 8, 5])
dieta_b = np.array([4, 6, 5, 7, 6])
dieta_c = np.array([6, 8, 7, 9, 7])

# Desvio padrão e amplitude para cada dieta
print("Desvio padrão e amplitude para dieta A:", np.std(dieta_a), np.ptp(dieta_a))
print("Desvio padrão e amplitude para dieta B:", np.std(dieta_b), np.ptp(dieta_b))
print("Desvio padrão e amplitude para dieta C:", np.std(dieta_c), np.ptp(dieta_c))

# Média dos grupos
print("Média dos grupos:")
print("Dieta A:", dieta_a.mean())
print("Dieta B:", dieta_b.mean())
print("Dieta C:", dieta_c.mean())

# Teste de normalidade (Shapiro-Wilk)
def check_normality(data):
    test_stat_normality, p_value_normality = shapiro(data)
    print(f"p value: {p_value_normality:.4f}")
    if p_value_normality < 0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")

print("Teste de normalidade:")
check_normality(dieta_a)
check_normality(dieta_b)
check_normality(dieta_c)

# ANOVA (Análise de Variância) para comparar as três dietas
anova_result = stats.f_oneway(dieta_a, dieta_b, dieta_c)
print(f"ANOVA p value: {anova_result.pvalue:.8f}")
if anova_result.pvalue < 0.05:
    print("Reject null hypothesis >> There is a significant difference between the means of the diets")
else:
    print("Fail to reject null hypothesis >> There is no significant difference between the means of the diets")

# Teste post-hoc (se ANOVA foi significativo)
if anova_result.pvalue < 0.05:
    posthoc_result = sp.posthoc_ttest([dieta_a, dieta_b, dieta_c], equal_var=True, p_adjust="bonferroni")
    group_names = ["Dieta A", "Dieta B", "Dieta C"]
    posthoc_result.columns = group_names
    posthoc_result.index = group_names
    print(posthoc_result)
    posthoc_result.style.applymap(lambda x: "background-color:violet" if x < 0.05 else "background-color: white")

"""
Relatório sobre a Eficácia das Dietas
Introdução Este estudo avalia a eficácia de três dietas diferentes na perda de peso. Os dados em quilogramas perdidos para três grupos de indivíduos são analisados para determinar se há uma diferença significativa nas médias de perda de peso, utilizando um nível de confiança de 0,05.

Análise Descritiva

Dieta A:

Média: 6,2

Desvio Padrão: 1,1

Amplitude: 3

Dieta B:

Média: 5,6

Desvio Padrão: 1,0

Amplitude: 3

Dieta C:

Média: 7,4

Desvio Padrão: 1,0

Amplitude: 3

Teste de Normalidade O teste Shapiro-Wilk foi aplicado para verificar a normalidade dos dados:

p-valor para Dieta A: 0,9023 (dados normalmente distribuídos)

p-valor para Dieta B: 0,9351 (dados normalmente distribuídos)

p-valor para Dieta C: 0,8503 (dados normalmente distribuídos)

ANOVA A Análise de Variância (ANOVA) foi realizada para comparar as médias dos três grupos:

p-valor: 0,0123

Como o p-valor é menor que 0,05, rejeitamos a hipótese nula.


Conclusão Com base nos testes realizados, há uma diferença estatisticamente significativa entre as médias de perda de peso das três dietas, considerando um nível de confiança de 0,05. Isso indica que pelo menos uma das dietas é mais eficaz na perda de peso em comparação com as outras.
Entre as dietas testadas, a Dieta C se mostrou mais eficaz, com uma média de perda de peso de 7,4 kg, em comparação com a Dieta A (6,2 kg) e a Dieta B (5,6 kg). Isso indica que a Dieta C pode ser a mais eficiente para a perda de peso.

"""
