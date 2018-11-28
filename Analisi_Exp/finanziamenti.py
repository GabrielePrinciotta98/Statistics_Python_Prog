import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

loans = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Analisi Esplorative/anexp/finanziamenti.csv', sep = ';', decimal = ',')
#print(loans)
"""
1)
print(loans['CodiceCategoria'])
#CARATTERE NOMINALE!!!

2)
print(loans['UNITA'].value_counts())

3)
loans['UNITA'].value_counts().plot.bar()
plt.show()

4)
4.1)
#L'intervallo [500000,4000000]
4.2)
#Circa 20-25 %

5)
5.1)
progetti_a = loans[loans['FinProvincia'] < loans['FinRegione']]
progetti_b = loans[loans['FinProvincia'] > loans['FinRegione']]
5.2)
print(progetti_a)
print(progetti_b)
#prgetti A = 368
#progetti B = 175

6)
6.1)
progetti_a = loans[loans['FinProvincia'] < loans['FinRegione']]
selezione_progetti_a = progetti_a[(progetti_a['FinProvincia'] >= 200) & (progetti_a['FinProvincia'] < 1000)]
print(selezione_progetti_a)
6.2)
bins = np.arange(min(selezione_progetti_a['FinProvincia']), max(selezione_progetti_a['FinProvincia']), 100)
print(bins)
selezione_progetti_a['FinProvincia'].hist(bins = bins)
plt.xticks(bins)
plt.show()
6.3)
selezione_progetti_a['FinProvincia'].plot.box()
plt.show()
6.4)
#????
6.5)
print(selezione_progetti_a['FinProvincia'].mean())
#MEDIA = 636.9
print(selezione_progetti_a['FinProvincia'].std())
#DEVIAZIONE STANDARD CAMPIONARIA = 264.80
#6.6)
finanziamenti_provinciali_tra_500_e_700 = loans[(loans['FinProvincia'] >= 500) & (loans['FinProvincia'] <= 700)]
print(finanziamenti_provinciali_tra_500_e_700['FinProvincia'].count())
#Risposta: 39
#6.7)
loans_with_data = loans.dropna()
finanziamenti_provinciali_with_data = loans_with_data['FinProvincia']
print(len(finanziamenti_provinciali_with_data))
tot_spese_with_data = loans_with_data['TotSpese']
print(len(tot_spese_with_data))
print(finanziamenti_provinciali_with_data.corr(tot_spese_with_data))
#INDICE DI CORRELAZIONE DI PEARSON = 0.68
plt.scatter(finanziamenti_provinciali_with_data, tot_spese_with_data)
plt.xlabel('finanziamenti provinciali')
plt.ylabel('Spese totali')
plt.show()
#6.8)
loans_with_data = loans.dropna()
finanziamenti_provinciali_no_outlier = loans_with_data[loans_with_data['FinProvincia'] < 1400000]
print(finanziamenti_provinciali_no_outlier)
tot_spese_no_outlier = loans_with_data[loans_with_data['TotSpese'] < 3400000]
print(tot_spese_no_outlier)
print(finanziamenti_provinciali_no_outlier['FinProvincia'].corr(tot_spese_no_outlier['TotSpese']))
#INDICE DI CORRELAZIONE DI PEARSON = 0.72
plt.scatter(finanziamenti_provinciali_no_outlier['FinProvincia'], tot_spese_no_outlier['FinProvincia'])
plt.show()

#7)
print(len(loans[loans['TotSpese'].isna()]))
#Risposta: 1134
"""
