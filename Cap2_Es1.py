import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studenti = np.arange(0,41,1)
qi = [114, 122, 103, 118, 99, 105, 134, 125, 117, 106,
     109, 104, 111, 127,133, 111, 117, 103, 120, 98,
     100, 130, 141, 119, 128, 106, 109, 115,113, 121,
     100, 130, 125, 117, 119, 113, 104, 108, 110, 102, 148]
studenti_qi = pd.Series(data = qi, index = studenti, dtype = int)
#print(studenti_qi)
studenti_qi_freq = pd.crosstab(index = studenti_qi,
                                columns = ['Abs.frequence'],
                                colnames = [' '],
                                rownames = ['QI'])

print(studenti_qi_freq)
studenti_qi.hist(bins = 10)
plt.show()
