import pandas as pd

df = pd.read_csv("netflix.csv")

df = df[df['type'] =='Movie']
df = df[df['country'] =='Brazil']

df['duration'] = df['duration'].map(lambda x: x.rstrip('min')).astype(int)

dataset = pd.DataFrame(df, columns=['listed_in','duration'])
dataset.columns = ['Categoria', 'Duracao']

dataset.to_csv("boxPlot.csv", index=False)