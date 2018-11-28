import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import statsmodels.api as sm
from paretochart.pareto import pareto

df_ospedali = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/csv_lab/dati-ospedali.csv', sep = ';')
#print(df_ospedali)
"""
dist = ECDF(df_ospedali['Medici SSN'])
#print(dist)
plt.plot(dist.x, dist.y)
plt.show()
df_ospedali['Medici SSN'].plot.hist()
plt.show()
"""



"""
sm.qqplot_2samples(df_ospedali['Medici SSN'], df_ospedali['Farmacisti SSN'], line = '45')
plt.show()
"""

grouped = df_ospedali.groupby('Regione') #raggruppa i valori della colonna regione
temp = grouped['Medici SSN'].sum()
pareto(temp, labels = temp.index)
plt.show()
