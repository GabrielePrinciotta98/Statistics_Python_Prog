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

5)
5.1)
print(cani['GravitaIP'])
#ORDINALE E NOMIANLE???
5.2)
#0, 1, 2, 3
5.3)
tab_GravitaIP_freq_rel = pd.crosstab(index = cani['GravitaIP'],
                                     columns = ['Freq. Relativa'],
                                     colnames = [' '],
                                     normalize = True)
print(tab_GravitaIP_freq_rel)
5.4)
cani['GravitaIP'].value_counts().plot.bar()
plt.show()

#6)
#6.1)
tab_Antiaritmico_freq_abs = pd.crosstab(index = cani['Antiaritmico'],
                                        columns = ['Freq. Assoluta'],
                                        colnames = [' '])
#print(tab_Antiaritmico_freq_abs)
#6.2)
#N° CANI CHE ASSUMONO UN FAMACO PER ARITMIA: 11
#6.3)
#SÌ:= 1, NO:= 0
#6.4)
print(cani['MC'].dropna())
tab_Antiaritmico_MC_freq_cong = pd.crosstab(index = cani['Antiaritmico'],
                                            columns = cani['MC'],
                                            colnames = ['MC'])
print(tab_Antiaritmico_MC_freq_cong)
#6.5)
#9/87 * 100 = 10.34%
"""
