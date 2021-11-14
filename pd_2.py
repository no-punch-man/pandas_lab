import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Anton\Downloads\flights.csv', sep = ',')
del df['Unnamed: 0']
labels = pd.unique(df['CARGO'])
width = 0.9
#number_of_flights
means = []
means.append(df[df.CARGO == 'Nimble']['CARGO'].size)
means.append(df[df.CARGO == 'Jumbo']['CARGO'].size)
means.append(df[df.CARGO == 'Medium']['CARGO'].size)

fig, ax = plt.subplots()
ax.bar(labels, means, width)
ax.set_title('Number of flights')
fig.savefig("Number of flights" + ".png")

#flights_cost
means_c = []
means_c.append(df[df.CARGO == 'Nimble']['PRICE'].sum())
means_c.append(df[df.CARGO == 'Jumbo']['PRICE'].sum())
means_c.append(df[df.CARGO == 'Medium']['PRICE'].sum())

fig, ax = plt.subplots()
ax.bar(labels, means_c, width)
ax.set_title('Summary costs of the flights')
fig.savefig("Summary costs of the flights" + ".png")

#flights_mass
means_m = []
means_m.append(df[df.CARGO == 'Nimble']['WEIGHT'].sum())
means_m.append(df[df.CARGO == 'Jumbo']['WEIGHT'].sum())
means_m.append(df[df.CARGO == 'Medium']['WEIGHT'].sum())

fig, ax = plt.subplots()
ax.bar(labels, means_m, width)
ax.set_title('Summary mass of the flights')
fig.savefig("Summary mass of the flights" + ".png")
