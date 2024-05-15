import sys
from itertools import groupby
from operator import itemgetter
import numpy as np
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)
data = read_mapper_output(sys.stdin)
for centroid_idx, points in groupby(data, itemgetter(0)):
    points = list(points)
    cluster_points = np.array([np.array(list(map(float, point[1].split(',')))) for point in points])
    new_centroid = np.mean(cluster_points, axis=0)
    print(f'{centroid_idx}\t{new_centroid.tolist()}')