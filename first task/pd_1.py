import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\Anton\Downloads\transactions.csv', sep = ',')
del df['Unnamed: 0']
#1 task
sorted_df = df.sort_values(by='SUM', ascending=False)
print(sorted_df[sorted_df.STATUS == 'OK'][0:3])
#2 task
series = (df.loc[(df.STATUS == 'OK') & (df.CONTRACTOR == 'Umbrella, Inc')]).SUM
print()
print(series.sum())
