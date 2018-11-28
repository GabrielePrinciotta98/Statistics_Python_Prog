import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


players = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/golfPlayers.csv')
#print(players)
scores_freq_rel = pd.crosstab(index = players['Punteggio'],
                              columns = ['Rel. freqence'],
                              colnames = [' '])

scores_freq_rel = scores_freq_rel / scores_freq_rel.sum()
scores_freq_rel.plot.bar()
plt.show()
