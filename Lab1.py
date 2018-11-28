import numpy as np
import pandas as pd

maglie = np.arange(1,24,1)
ngol = np.random.randint(0,30, size=23)
gol = pd.Series(data= ngol, index=maglie, name='gol', dtype=int)
print("Serie: ")
print(gol)

print("Capocannoniere:",gol.max())
golcresc = gol.sort_values()

print("Primi 5 capocannonieri:")
print(golcresc[-5:])

print("Ultimi 5 capocannonieri:")
print(golcresc[:5])

print("0 gol:")
print(gol[gol==0])

print("11 titolari:")
print(gol[0:11] == 0)

print("Riserve")
print(gol[-12:] == 0)

print("Attaccanti:")
print(gol[8:11] == 0)

print("gol dei numeri 5,9,10,14:")
print(gol[5] + gol[9] + gol[10] + gol[14])

print(gol.sort_index(ascending = False))
