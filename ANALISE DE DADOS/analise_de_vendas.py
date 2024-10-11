import pandas as pd

tabela = pd.read_excel('Vendas.xlsx') #lendo a tabela com o pandas
print(tabela)

faturamento_total = tabela["Valor Final"].sum() #acessar a coluna valor final para faszer o calculo de faturamento global dos produtos
print(faturamento_total)

faturamento_por_loja = tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

faturamento_por_produto = tabela[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja","Produto"]).sum()
print(faturamento_por_produto)