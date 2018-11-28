import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_capelli = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/csv_lab/capelli.csv')
#print(df_capelli)
corr_capelli = df_capelli.corr()
#print(corr_capelli['lunghezzaCapelli'])
#capelli_normalize = pd.crosstab(index = df_capelli['lunghezzaCapelli'],
#                                columns = df_capelli['spesaShampoMensile'],
#                                normalize = 'columns')
#print(capelli_normalize)
#df_capelli.plot.scatter('lunghezzaCapelli', 'spesaShampoMensile')
#df_capelli.plot.scatter('lunghezzaCapelli', 'spesaTaglioMensile')
#df_capelli.plot.scatter('lunghezzaCapelli', 'probFidanzamento')
#plt.show()
df_capelli['spesaShampoMensile'].plot.box()
plt.show()
df_capelli['spesaShampoMensile'].plot.hist()
plt.show()
