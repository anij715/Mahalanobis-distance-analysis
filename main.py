#import functions
import numpy as np
import pandas as pd
from numpy.linalg import inv
from scipy.spatial import distance
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity


#define two vectors

d1 = [8, 10, 10, 8, 7, 10, 9, 7, 1]
d2 = [1,1,1,1,1,1,3,1,1]
d3 = [3,4,5,2,6,8,4,1,1]
d4 = [10,10,10,3,10,10,9,10,1]
d5 = [10,10,10,10,10,10,4,10,10]

a = np.asarray([d1,d2,d3,d4,d5])


data = pd.read_csv("HW1-win-data.csv")
data.drop(data.columns[[0,1,11]], axis = 1, inplace=True)

iv = inv(np.cov(data, rowvar=False))
#print(iv)


for i in range(5):
	for j in range(i+1,5):
		out3 = distance.mahalanobis(a[i], a[j], iv)
		print(out3)


out1 = euclidean_distances(a,a)
out2 = cosine_similarity(a,a)

print(out1)
print(out2)