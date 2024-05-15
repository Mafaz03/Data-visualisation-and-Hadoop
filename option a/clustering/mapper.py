import sys
import numpy as np
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

for line in sys.stdin:
    point = np.array(list(map(float, line.strip().split(','))))
    min_dist = float('inf')
    closest_centroid_idx = None
    centroids = [1,3,5]  # List of centroids
    for idx, centroid in enumerate(centroids):
        dist = euclidean_distance(point, centroid)
        if dist < min_dist:
            min_dist = dist
            closest_centroid_idx = idx
    print(f'{closest_centroid_idx}\t{line.strip()}')