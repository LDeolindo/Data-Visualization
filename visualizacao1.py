import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv 


df = pd.read_csv("netflix.csv")

grafico = df.groupby(['country', 'release_year']).size().sort_values(ascending=False).reset_index(name='count')
# print(grafico)

paises = grafico.iloc[:, 0].values
ano = grafico.iloc[:, 1].values
valor = grafico.iloc[:, 2].values

print(paises)
print(ano)
print(valor)

# def remove_repetidos(li):
#     return sorted(dict(zip(li, li)).keys())


vetAno = set(ano)
vetAno = list(vetAno)
vetAno.insert(0, 'country')

with open("novos.csv", "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames = vetAno)
    writer.writeheader()
    vetPaises = set(paises)
    vetPaises = list(vetPaises)
    
    for i in vetPaises: 
        line = ''
        line += "\"" + i + "\"" + ","
        for j in vetAno:
            flag = -1
            for k in range(0, len(paises) -1):
                if(ano[k] == j and paises[k] == i and flag == -1):
                    line += str(valor[k]) + ","
                    flag = 0
            if(flag == -1):
                line += "0,"
        csv_file.write(line)
        csv_file.write('\n')
