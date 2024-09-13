import numpy as np
import pandas as pd
import banco_de_dados as bd
from funcoes import Funcoes_Estatisticas

# Importando os dados do banco de dados
#dados1 = bd.sync
#dados2 = bd.asyncr
dados1 = bd.iris['Id']
dados2 = bd.stock['Open']
# Criando uma instância da classe Funcoes_Estatisticas
estatisticas = Funcoes_Estatisticas(dados1, dados2, variancia_tipo='populacional')

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1: Para saber a média de dados1 e dados2")
        print("2: Para saber a mediana de dados1 e dados2")
        print("3: Para saber o primeiro e terceiro quartil de dados1 e dados2")
        print("4: Para saber a moda de dados1 e dados2")
        print("5: Para saber a amplitude de dados1 e dados2")
        print("6: Para saber a amplitude interquartil de dados1 e dados2")
        print("7: Para saber a variância de dados1 e dados2")
        print("8: Para saber o desvio padrão de dados1 e dados2")
        print("9: Para saber o mínimo, máximo e a subtração dos valores de dados1 e dados2")
        print("10: Para mostrar o intervalo de classes dos dados1 e dados2")
        print("11: Para identificar outliers em dados1 e dados2")
        print("12: Plota boxplots para os dois conjuntos de dados (dados1 e dados2)")
        print("0: Sair")

        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            print(estatisticas.media())
        elif escolha == '2':
            print(estatisticas.mediana())
        elif escolha == '3':
            print(estatisticas.percentil())
        elif escolha == '4':
            print(estatisticas.moda())
        elif escolha == '5':
            print(estatisticas.amplitude())
        elif escolha == '6':
            print(estatisticas.amplitude_interquartil())
        elif escolha == '7':
            print(estatisticas.variancia())
        elif escolha == '8':
            print(estatisticas.desviopadrao())
        elif escolha == '9':
            print(estatisticas.min_e_max())
        elif escolha == '10':
            estatisticas.intervalo_de_classes()
        elif escolha == '11':
            print(estatisticas.outliers())
        elif escolha == '12':
            print(estatisticas.boxplot())
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 0 e 12.")

def main():
    menu()
    

if __name__ == "__main__":
    main()