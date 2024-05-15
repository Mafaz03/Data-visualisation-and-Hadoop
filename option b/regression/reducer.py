import sys
import numpy as np

all = []

for data in sys.stdin:
    line = data.strip().split('\t')
    _, x, y, x2, xy = map(float, line)
    all.append([x, y, x2, xy])

all_np = np.asarray(all)
sum_x, sum_y, sum_x2, sum_xy = all_np.sum(0)
count = len(all_np)

print("Count:", count)
print("Sum_x:", sum_x)
print("Sum_y:", sum_y)
print("Sum_x2:", sum_x2)
print("Sum_xy:", sum_xy)

beta_1 = (count * ((sum_xy) - (sum_x * sum_y))) / ((count * (sum_x2) - (sum_x**2)))
beta_0 = (sum_y - (beta_1 * sum_x)) / count

print("Coefficients (beta_0, beta_1):", beta_0, beta_1)