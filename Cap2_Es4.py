import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_qualita_aria = pd.read_csv('/home/gabriele/Documenti/Università/Statistica/Dataset/qualita_aria.csv')
print(df_qualita_aria)
df_qualita_aria.plot.scatter('2000', '2002')
plt.show()
