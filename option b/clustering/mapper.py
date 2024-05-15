import sys
import numpy as np
import math

centroids = [1,3,5]
for line in sys.stdin:
    a = line.strip().split(',')[:2]
    points = [float(b) for b in a]
    point1, point2 = points

    min_dist = float('inf')
    min_centroid = None
    for centroid in centroids:
        dist = math.sqrt(((point1 - centroid)**2 + (point2 - centroid)**2))
        if dist < min_dist:
            min_dist = dist
            min_centroid = centroid
    print(min_centroid,',', point1,',',point2)
