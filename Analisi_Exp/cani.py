import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from paretochart.pareto import pareto
from sklearn import metrics


cani = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Analisi Esplorative/anexp/cani.csv', sep = ';', decimal = ',')
#print(cani) #N° RECORD: 161

"""
                    ESERCIZIO A

1)
#cani.info()
#N° CANI SEGUITI: 161

2)
print(cani[cani['IP'] == 'SI'])
#N° CANI CHE SOFFRONO DI IPERTENSIONE: 58

#3)
#3.1)
cani_eta = cani['EtaAnni']
print(cani_eta)
bins = np.arange(int(min(cani_eta)), (max(cani_eta)) + 1, 1)
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
#[12,13)

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

#5)
#5.1)
print(cani['GravitaIP'])
#ORDINALE
#5.2)
print(cani['GravitaIP'].unique())
#0, 1, 2, 3
#5.3)
tab_GravitaIP_freq_rel = pd.crosstab(index = cani['GravitaIP'],
                                     columns = ['Freq. Relativa'],
                                     colnames = [' '],
                                     normalize = True)
print(tab_GravitaIP_freq_rel)
#5.4)
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

#7)
#7.1)
#Il 60%
#7.2)
#10%-15%
#7.3)
print(cani['SURVIVALTIME'])
#bins = np.arange(min(cani['SURVIVALTIME']), max(cani['SURVIVALTIME']), 365)
#cani['SURVIVALTIME'].hist(bins = bins)
#plt.xticks(bins)
#plt.show()
#7.4)
#print(cani['SURVIVALTIME'].quantile(0.25))
#print(cani['SURVIVALTIME'].quantile(0.75))
#113, 711
#7.5)
#print(len(cani[(cani['SURVIVALTIME'] >= 113) & (cani['SURVIVALTIME'] <= 711)]))
#81
#7.6)
bins2 = np.arange(113, 813, 100)
cani_interquartili = cani[(cani['SURVIVALTIME'] >= 113) & (cani['SURVIVALTIME'] <= 711)]
cani_interquartili['SURVIVALTIME'].hist(bins = bins2)
plt.xticks(bins2)
#plt.show()
#7.7)
#????????????
#7.8)
print(cani['SURVIVALTIME'].mean())
#MEDIA: 459.89, CIRCA 460
#7.9)
print(cani['SURVIVALTIME'].std())
#DEVIAZIONE STANDARD CAMPIONARIA: 467.20

#8)
print(cani['Allodiast'])
#8.1)
#bins3 = np.arange(min(cani['Allodiast']), max(cani['Allodiast']), 0.2)
#cani['Allodiast'].hist(bins = bins3)
#plt.xticks(bins3)
#plt.show()
#NON È NORMALE
#8.2)
#??????????????

#9)
#print(cani['EDVI'].dropna())
plt.scatter(cani['Allodiast'], cani['EDVI'])
plt.show()
print(cani['Allodiast'].corr(cani['EDVI']))
#NON SONO INDIPENDENTI (INDICE DI CORRELAZIONE DI 0.90!!)

#            ESERCIZIO B

cani_morti = cani[cani['MORTE'] == 1]
#print(cani_morti)
cani_morti_with_MC_and_OndaEA = cani_morti[(cani_morti['MC'].notna()) & (cani_morti['OndaEA'].notna())]
#print(cani_morti_with_MC_and_OndaEA)

#1)
#print(cani_morti_with_MC_and_OndaEA['OndaEA'])
#ORDINALE (MA ANCHE SCALARE???)

#2)
#cani_morti_with_MC_and_OndaEA['OndaEA'].plot.box()
#plt.show()

#3)
#print(cani_morti_with_MC_and_OndaEA[cani_morti_with_MC_and_OndaEA['OndaEA'] > 4.0])
#4.19

#4)
#SI

#5)
cani_morti_altre_cause = cani_morti_with_MC_and_OndaEA[cani_morti_with_MC_and_OndaEA['MC'] == 0.0]
s = cani_morti_altre_cause['OndaEA'].quantile(0.75)
#print(s)

#6)
cani_morti_cause_cardiache = cani_morti_with_MC_and_OndaEA[cani_morti_with_MC_and_OndaEA['MC'] == 1.0]
#print(len(cani_morti_cause_cardiache))
#print(len(cani_morti_altre_cause))
#CAUSE CARDIACHE: 66
#ALTRE CAUSE: 17

#7)
print(len(cani_morti_cause_cardiache[cani_morti_cause_cardiache['OndaEA'] >= s]))
print(len(cani_morti_altre_cause[cani_morti_altre_cause['OndaEA'] < s]))
#N° MORTI CAUSE CAARDIACHE: 41
#N° MORTI ALTRE CAUSE: 12

#8)
var = cani_morti_with_MC_and_OndaEA
print(var)
vp = len(var[(var['OndaEA'] >= s) & (var['MC'] == 1)])
fp = len(var[(var['OndaEA'] >= s) & (var['MC'] == 0)])
vn = len(var[(var['OndaEA'] < s) & (var['MC'] == 0)])
fn = len(var[(var['OndaEA'] < s) & (var['MC'] == 1)])
print(vp, fp, vn ,fn)

sens = vp / (vp + fn)
spec = vn / (vn + fp)
print(sens, spec)

preds = var['OndaEA'] >= s
fpr, tpr, _ = metrics.roc_curve(var['MC'], preds)

plt.plot(fpr, tpr)
plt.plot([0,1], [0,1], dashes = [3,3], color = 'gray')
plt.xlim([-0.01, 1])
plt.ylim([0, 1.01])
plt.axis('equal')

plt.show()
"""
