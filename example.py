# coding: utf-8
import sys
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

import kmedoids
for arg in sys.argv:
    print(arg)
numberofclusters=int(sys.argv[1])
#int(sys.argv[0])
text_file = open("locpoint.txt", "r")
lines = text_file.read().split(',')
text_file.close()
length=len(lines)
data=np.array(lines).reshape(int(length/2),2)
data=data.astype('float32',casting='unsafe')

outputar=np.array([])
# distance matrix
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = kmedoids.kMedoids(D, numberofclusters)
'''  
if M is not None:
    M, C = kmedoids.kMedoids(D, numberofclusters)
    if M is not None:
        M, C = kmedoids.kMedoids(D, numberofclusters)
        if M is not None:
            raise Exception('too many medoids (after removing duplicate points)')
'''
#file=open("output.txt","w")
print('medoids:')
for point_idx in M:
    outputar=np.concatenate((outputar,data[point_idx]),axis=0)
np.savetxt('medoid.txt',M,fmt="%s")
np.savetxt('output.txt',outputar,fmt="%s",delimiter=',')    
print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))

