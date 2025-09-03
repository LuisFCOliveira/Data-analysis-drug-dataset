import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./drugs.csv")  # base de dados drogas

# df = df.iloc[:,[0,2,6]]       # ficar com colunas 0,2,6
print(df.shape) #(663, 130)
print(df.head(),"\n")
print(df.columns,"\n")
print(df.describe(),"\n")


##### Ex: State
state = df["State"]

print('Alabama' in np.unique(state.values))
np.unique(pd.isnull(state))
print(state.name)
print(state.index)
print(type(df))


### Remover valores nulos

df.dropna(how='all') #remove linhas com algum valor nulo, com all remove apenas linhas com total valores nulos
df[df.notnull()]
#np.dropna(thresh=3) mantém linhas que tenham apenas um certo número de observações

#df.filna() substitui valores nulos pelo valor inserido
# é possível com um dicionário determinar cada valor
# df.fillna({1: 0.5, 3: -1})

