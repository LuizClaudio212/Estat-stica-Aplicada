import banco_de_dados as bd  # Importa módulo com dados das espécies de iris.
import pandas as pd 
"""
1. Qual espécie de iris (Setosa, Versicolor, Virginica) tem a maior média de comprimento de pétala?
"""

# Extrai o comprimento das pétalas para cada espécie.
setosa = bd.setosa['PetalLengthCm']  
versicolor = bd.versicolor['PetalLengthCm']  
virginica = bd.virginica['PetalLengthCm']  

def media(setosa, versicolor, virginica):
    """
    Calcula a média do comprimento das pétalas para cada espécie.

    Parâmetros:
    - setosa: Comprimento das pétalas da espécie Setosa.
    - versicolor: Comprimento das pétalas da espécie Versicolor.
    - virginica: Comprimento das pétalas da espécie Virginica.

    Retorna:
    - Uma tupla com as médias formatadas.
    """
    setosa = setosa.mean()  # Média de Setosa.
    versicolor = versicolor.mean()  # Média de Versicolor.
    virginica = virginica.mean()  # Média de Virginica.
    return (f"Média de setosa: {setosa:.2f}CM", 
            f"Média de versicolor: {versicolor:.2f}CM", 
            f"Media de virginica: {virginica:.2f}CM")  

print(media(setosa, versicolor, virginica))  # Imprime as médias calculadas.
