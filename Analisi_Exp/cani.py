import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cani = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Analisi Esplorative/anexp/cani.csv', sep = ';', decimal = ',')
#print(cani)

"""
1)
#N° CANI SEGUITI: 161

2)
print(cani[cani['IP'] == 'SI'])
#N° CANI CHE SOFFRONO DI IPERTENSIONE: 58

#3)
#3.1)
cani_eta = cani['EtaAnni']
print(cani_eta)
bins = np.arange(min(cani_eta), max(cani_eta), 1)
cani_eta.hist(bins = bins)
plt.show()
#3.2)
print(cani_eta.median())
print(min(cani_eta))
print(max(cani_eta))
print(cani_eta.var())
#MEDIANA: 12.55
#MINIMO: 1.22
#MASSIMO: 16.84
#VARIANZA: 6.91
#3.3)
print(len(cani_eta[(cani_eta >= 12) & (cani_eta < 13)]))
#N° CANI DI ETA COMPRESA TRA 12(INCLUSO) E 13(ESCLUSO): 32
#3.4)
#CANE PIÙ ANZIANO: 16.84
#3.5)
#[12.23, 14,23)

#4)
#4.1)
cani_morti = cani[cani['MORTE'] == 1]
print(cani_morti)
#N° CANI DECEDUTI: 118
#4.2)
cani_morti_cardio_with_NaN = cani_morti['MC']
#print(cani_morti_cardio_with_NaN)
cani_morti_NaN = len(cani_morti_cardio_with_NaN) - len(cani_morti_cardio_with_NaN.dropna())
#print(cani_morti_NaN)
#NO, N° CANI MORTI SENZA CAUSA INSERITA: 3
#4.3)
incongruenze_morte = len(cani[(cani['MORTE'] == 0) & (cani['MC'] == 1.0)])
#print(incongruenze_morte)
#N° INCONGRUENZE: 0
#4.4)
cani_morti_cardio = cani_morti[cani_morti['MC'] == 1.0]
print(cani_morti_cardio)
print(len(cani_morti_cardio))
#N° CANI MORTI PER CAUSE CARDIACHE: 87
print(np.round((len(cani_morti_cardio) / len(cani_morti)) * 100, 2), '%')
#PERCENTUALE CANI MORTI PER MORTE CARDIACA: 73.73%
"""
