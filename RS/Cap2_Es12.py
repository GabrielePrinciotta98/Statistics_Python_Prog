import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

precipitazioni = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/precipitazioni.csv')
#print(precipitazioni)


#-----12-----
#precipitazioni_freq_rel_gen = pd.crosstab(index = precipitazioni['Gen'],
#                                            columns = ['Abs. freqence'],
#                                            colnames = [' '],
#                                            normalize = True)
#print(precipitazioni_freq_rel_gen)
#precipitazioni_freq_rel_gen.plot(marker = 'o', legend = False)
#plt.show()


#-----13-----
#precipitazioni_primi_12 = precipitazioni[:12]
#print(precipitazioni_primi_12)
#precipitazioni_primi_12_freq_abs_nov = pd.crosstab(index = precipitazioni_primi_12['Nov'],
#                                                    columns = ['Abs.freqence'],
#                                                    colnames = [' '])
#print(precipitazioni_primi_12_freq_abs_nov.sort_values(by = 'Abs.freqence', ascending = False))


#-----14-----

precipitazioni_primi_24 = precipitazioni[:24]
#print(precipitazioni_primi_24)
precipitazioni_primi_24_freq_rel_giu = pd.crosstab(index = precipitazioni_primi_24['Giu'],
                                                    columns = ['Abs.freqence'],
                                                    colnames = [' '],
                                                    normalize = True)
#print(precipitazioni_primi_24_freq_rel_giu)
precipitazioni_primi_24_freq_rel_dic = pd.crosstab(index = [precipitazioni_primi_24['Dic'], precipitazioni_primi_24['Set']],
                                                    columns = ['Abs.freqence'],
                                                    colnames = [' '],
                                                    normalize = False)
print(precipitazioni_primi_24_freq_rel_dic)
precipitazioni_primi_24_freq_rel_giu_plt = (pd.crosstab(index = precipitazioni_primi_24['Giu'],
                                                    columns = ['Abs.freqence'],
                                                    colnames = [' '],
                                                    normalize = True)).loc[:,'Abs.freqence']

precipitazioni_primi_24_freq_rel_dic_plt = (pd.crosstab(index = precipitazioni_primi_24['Dic'],
                                                    columns = ['Abs.freqence'],
                                                    colnames = [' '],
                                                    normalize = True)).loc[:,'Abs.freqence']

#precipitazioni_primi_24_freq_rel_dic_plt.plot(marker = 'o', color = 'blue')
#precipitazioni_primi_24_freq_rel_giu_plt.plot(marker = 'o', color = 'black')
#plt.show()

#precipitazioni_primi_24_freq_rel_giu_plt.plot.bar(color = 'blue', alpha = 0.7)
#precipitazioni_primi_24_freq_rel_dic_plt.plot.bar(color = 'red', alpha = 0.7)
#plt.show()
