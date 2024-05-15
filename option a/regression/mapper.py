import sys

for data in sys.stdin:
    data = data.strip().split(',')
    # Skip lines that cannot be converted to floats
    try:
        x, y = map(float, data)
    except ValueError:
        continue
    # Emit (1, x, y, x^2, xy) key-value pairs
    print("%d\t%f\t%f\t%f\t%f" % (1, x, y, x**2, x*y))