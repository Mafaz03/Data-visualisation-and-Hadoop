import sys
from collections import Counter

all = []

for line in sys.stdin:
    word, count = line.strip().split("\t")
    all.append(word)

sorted_counted = dict(Counter(all))
keys = list(sorted_counted.keys())
for key in keys:
    print(key, "  " ,sorted_counted[key])
