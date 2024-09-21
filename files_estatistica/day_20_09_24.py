import numpy as np
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats
import banco_de_dados as bd


dados1 = bd.sync
dados2 = bd.asyncr
"""
Teste de hipotese

Teste de normalidade (shapiro-wilk)

Ho e a hipotese 
"""

p,p1 = scipy.stats.shapiro(dados1)

q,q1 = scipy.stats.shapiro(dados2)


if p1 < 0.5:
    print("Rejeitar h0")
else:
    print("Não rejeitar h0")

if q1 < 0.5:
    print("Rejeitar h0")
else:
    print("Não rejeitar h0")
# aprox 0 = sintonia, >0 calda a direita, <0 calda a esquerda
sk1 = scipy.stats.skew(dados1)
sk2 = scipy.stats.skew(dados2)

print(sk1)
print(sk2)
