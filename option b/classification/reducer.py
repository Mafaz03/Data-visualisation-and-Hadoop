import sys
import pandas as pd

cause_total = {}
all = []
#Partitoner
for line in sys.stdin:
    line = line.strip()
    state, cause, total = line.split('\t')
    total = int(total)
    all.append([cause + " : " + state, total])

df = pd.DataFrame(all)
result = df.groupby(0).sum().reset_index()

pd.set_option('display.max_rows', None)
print(result)
