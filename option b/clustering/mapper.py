import sys
import numpy as np

centroids = [1,3,5]
for line in sys.stdin:
    point1, point2 = map(float, line.strip().split(','))

    min_dist = float('inf')
    min_centroid = None
    for centroid in centroids:
        dist = ((point1 - centroid ) + (point2 - centroid))**2
        if dist < min_dist:
            min_dist = dist
            min_centroid = centroid
    print(min_centroid,',', point1,',',point2)