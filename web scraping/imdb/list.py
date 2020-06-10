import pandas as pd

#List average earnings (Gross USA) of each Genre in descending order.

df = pd.read_csv('IMDB.csv')
pd.set_option('display.max_rows', None)
grouped = df.groupby('genre', as_index=False)['gross_USA'].mean()
print(grouped.sort_values('gross_USA', ascending=False).astype(str))