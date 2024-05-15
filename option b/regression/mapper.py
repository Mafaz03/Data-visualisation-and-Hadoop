import sys

for data in sys.stdin:
    data = data.strip().split(',')
    x, y = map(float, data) 
    print("%d\t%f\t%f\t%f\t%f" % (1, x, y, x**2, x*y))
    print(f"{1}\t{x}\t{y}\t{x**2}\t{x+y}")