import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv 


df = pd.read_csv("netflix.csv")

paises = df.groupby(['country']).size().groupby(level=0).max()
paises.to_csv("paises.csv")

anoLancamento = df.groupby(['release_year']).size().groupby(level=0).max()
anoLancamento.to_csv("anoLancamento.csv")

categoria = df.groupby(['listed_in']).size().groupby(level=0).max()
categoria.to_csv("categoria.csv")

tipo = df.groupby(['type']).size().groupby(level=0).max()
tipo.to_csv("tipo.csv")