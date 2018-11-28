import pandas as pd
import numpy as np

ospedali = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/csv_lab/dati-ospedali.csv', sep = ';')
#print(ospedali)
"""
regioni_freq_abs = pd.crosstab(index = ospedali['Regione'],
                                columns = ['Abs.freqence'],
                                colnames = [' '])
regioni_freq_rel = pd.crosstab(index = ospedali['Regione'],
                                columns = ['Rel.freqence'],
                                colnames = [' '],
                                normalize = True)
print (regioni_freq_abs)
print (regioni_freq_rel)
"""
"""
print(ospedali['Regione'].value_counts())
print(ospedali['Regione'].value_counts() / ospedali['Regione'].value_counts().sum())
"""

"""
medici_minori = ospedali[ospedali['Medici SSN'] < 200]
print(medici_minori[['Denominazione Str. Pubblica New', 'Medici SSN']])
"""

"""
ospedali_lombardia = ospedali[ospedali['Regione'] == 'Lombardia']
print(ospedali_lombardia[['Denominazione Str. Pubblica New', 'Regione']])
"""
"""
ospedali_campania = ospedali[ospedali['Regione'] == 'Campania']
print(ospedali_campania['Ingegneri SSN'].mean())
"""
"""
medici_minori_400 = ospedali[ospedali['Medici SSN'] > 400]
varianza = medici_minori_400['Assistenti sociali SSN'].var()
print(varianza)
"""
"""
ospedale_minimo = ospedali[ospedali['Medici SSN'] == ospedali['Medici SSN'].min()]
print(ospedale_minimo['Denominazione Str. Pubblica New'])
"""
"""
ospedali_ordinati = ospedali.sort_values(by = 'Medici SSN',ascending = False)
print(ospedali_ordinati[['Denominazione Str. Pubblica New', 'Medici SSN']][:10])
"""

odontoiatri_presenti = ospedali['Odontoiatri Universitari'].dropna()
print(odontoiatri_presenti)

odontoiatri_presenti_maggiore_0 = odontoiatri_presenti[odontoiatri_presenti > 0]
print(odontoiatri_presenti_maggiore_0.count())
