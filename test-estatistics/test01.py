import numpy as np
import statistics as sta

#Dados
sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6]) # 22
asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2]) # 14


#media dos dados
def media(dados1, dados2):
    #media sync
    x = dados1.mean()
    print(f"Media sync: {x}")

    #media asyncr
    x2 = dados2.mean()
    print(f"Media asyncr: {x2}")

#mediana dos dados
def mediana(dados1, dados2):
    #mediana sync
    x = np.median(dados1)
    print(f"Mediana sync: {x}")
    
    #mediana asyncr
    x2 = np.median(dados2)
    print(f"Mediana asyncr: {x2}")    

def percentil(dados1, dados2):
    #pn = posição do percentil
    #pn = np.percentile (dados, percentual)
    print(f"1 Quartil sync: {np.percentile(dados1, 25)}")
    print(f"3 Quartil sync: {np.percentile(dados1, 75)}")
    print(f"1 Quartil asyncr: {np.percentile(dados2, 25)}")
    print(f"3 Quartil asyncr: {np.percentile(dados2, 75)}")    


def moda(dados1, dados2):
    #moda dos dados
    x = sta.multimode(dados1)
    print(f"Moda de sync: {x}")
    x2 = sta.multimode(dados2)
    print(f"Moda de asyncr: {x2}")
    
 

def amplitude(dados1, dados2):
    #sofre influencia de possiveis valores atipicos (outliers)
    #amplitude dos dados
    x = np.ptp(dados1)
    print(f"Amplitude sync: {x}")
    x2 = np.ptp(dados2)
    print(f"Amplitude asyncr: {x2}")
    

def amplitude_interquartil(dados1, dados2):
    #amplitude interquartil dos dados (porcentagem especifica dos valores)
    q1 = np.percentile(dados1, 25)
    print(f"Amplitudade de 25% do sync: {q1}")
    q3 = np.percentile(dados1, 75)
    print(f"Amplitudade de 50 ate 75% do sync: {q3}")
    
    #IQR = Q3 - Q1 IQR não sofre influência de valores atipicos (outliers)
    IQR1 = q3 - q1
    print(f"IQR Sync: {IQR1}")
    
    #mesmo coinceito para os dados da segunda array
    v1 = np.percentile(dados2, 25)
    print(f"Amplitudade de 25% do asyncr: {v1}")
    v3 = np.percentile(dados2, 75)
    print(f"Amplitudade de 50 ate 75% do asyncr: {v3}")
    
    IQR2 = v3 - v1
    print(f"IQR Asyncr: {IQR2}")
    
    

print(media(sync, asyncr))

print(mediana(sync, asyncr))

print(percentil(sync, asyncr))

print(moda(sync, asyncr))

print(amplitude(sync, asyncr))

print(amplitude_interquartil(sync, asyncr))