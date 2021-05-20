import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix.csv")

df2 = df[df['type'] =='TV Show']
df2 = df[df['country'] =='Brazil']

# df = df[df['type'] =='TV Show']
df = df[df['type'] =='Movie']
df = df[df['country'] =='Brazil']

filter = df[df.cast != ''].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)

dataset = pd.DataFrame(filter, columns=['title'])
dataset.columns = ['cast']

cast_mov = dataset.groupby(['cast']).size().groupby(level=0).max().reset_index(name='count_mov')


filter2 = df2[df2.cast != ''].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)

dataset2 = pd.DataFrame(filter2, columns=['title'])
dataset2.columns = ['cast']

cast_ser = dataset2.groupby(['cast']).size().groupby(level=0).max().reset_index(name='count_ser')


merged_inner = pd.merge(left=cast_mov, right=cast_ser, left_on='cast', right_on='cast')
# In this case `species_id` is the only column name in  both dataframes, so if we skipped `left_on`
# And `right_on` arguments we would still get the same result

# What's the size of the output data?
merged_inner.shape
merged_inner

merged_inner.to_csv("inner.csv", index=False)