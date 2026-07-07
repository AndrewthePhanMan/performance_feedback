from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

distance, path = fastdtw(recording, reference, dist=euclidean)