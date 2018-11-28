import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
'Captain America', 'Daredavil', 'Elektra', 'Flash',
'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
'Mystique', 'Professor X', 'Rogue', 'Superman',
'Spider-Man', 'Thor', 'Northstar']

years = [1941,1962,None,None, 1941,
1964,None,1940,1941,1961,
None,1963,None,1963,1981,None,None,1962,1979]

counts = {}

for y in years:
    if y in counts:
        counts[y] += 1
    else:
        counts[y] = 1

#print(counts)

pairs = list(counts.items())
print(pairs)
print(pairs[1])
pairs.sort(key = lambda pairs:pairs[1], reverse = True)
print("Ordinati: ")
print(pairs)
