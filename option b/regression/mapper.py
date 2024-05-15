import sys

for data in sys.stdin:
    data = data.strip().split(',')
    x, y = map(float, data) 
    print(f"{1}\t{x}\t{y}\t{x**2}\t{x*y}")
