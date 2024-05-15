import sys
import numpy as np
import pandas as pd

all = []

for data in sys.stdin:
    line = data.strip().split(',')
    centroid, x, y = map(float, line)
    all.append([centroid, x, y])
# print(all)
centroid_new = pd.DataFrame(all).groupby(0).mean()
for _, row in centroid_new.iterrows():
    print("New Centroid (x,y): ", row[1], row[2])