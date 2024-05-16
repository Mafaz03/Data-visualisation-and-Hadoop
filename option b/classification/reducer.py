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

#If the pandas not installed
# import sys

# all = []

# for lines in sys.stdin:
#     state,cause,death = lines.strip().split("\t")
#     all.append([(state + ' : ' + str(cause)),death])

# d = {}
# for i in all:
#     if i[0] not in all:
#         d[i[0]] = i[1]
#     else:
#         d[i[0]] += i[1]
# idx = d.keys()
# for i in idx:
#     print(i,d[i])
