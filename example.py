# coding: utf-8
from decimal import Decimal, ROUND_DOWN
import googlemaps
import sys
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
#import urllib.request
import kmedoids
gmaps=googlemaps.Client(key='AIzaSyBDYmw6Lhc8z27r7UM4FUXTo_5vQrKZC5Q')
datainput=""
tempdata=[]
import pprint
numberofclusters=int(sys.argv[1])
#int(sys.argv[0])
text_file = open("locpoint.txt", "r")
lines = text_file.read().split(',')
text_file.close()
length=len(lines)
data=np.array(lines).reshape(int(length/2),2)
data=data.astype('float32',casting='unsafe')
for i in range(0,length,2):
    #x = Decimal(str(lines[i])).quantize(Decimal('.000001'), rounding=ROUND_DOWN)
    #y = Decimal(str(lines[i+1])).quantize(Decimal('.000001'), rounding=ROUND_DOWN)
    x=float(lines[i])
    x=round(x,4)
    y=float(lines[i+1])
    y=round(y,4)
    origin={"lat":y, "lng":x}
    tempdata.append(origin)
#print(tempdata)
    #np.append(tempdata,datainput)
#print(tempdata)






outputar=np.array([])
tempdata2=tempdata
D = np.array([]).reshape(0,int(length/2))
# distance matrix
#D = pairwise_distances(data, metric='euclidean')
Dist=gmaps.distance_matrix(tempdata,tempdata2)
# split into 2 clusters
#pprint.pprint(Dist["rows"])
Dist=Dist["rows"]


for row in Dist:
    #print(row)
    inputar=np.array([[]])
    #row=row["elements"]
    for items in row.items():
        a=1
        #items=items[1]
        #print("PRINTING-----")
        items=items[1]
        #print(items)
        inputar=np.array([])
        for val in items:
            #print("PRINTING-----")
            val=val["distance"]
            values=val["value"]
            inputar=np.append(inputar,values)
        #tempar=np.array([inputar])
        D=np.vstack([D,inputar])
        #D=D.reshape(int(length/),int(length/2))


'''  
if M is not None:
    M, C = kmedoids.kMedoids(D, numberofclusters)
    if M is not None:
        M, C = kmedoids.kMedoids(D, numberofclusters)
        if M is not None:
            raise Exception('too many medoids (after removing duplicate points)')
'''
#file=open("output.txt","w")

M, C = kmedoids.kMedoids(D, numberofclusters)
#print(C)
print('medoids:')
for point_idx in M:
    outputar=np.concatenate((outputar,data[point_idx]),axis=0)
np.savetxt('medoid.txt',M,fmt="%s")
np.savetxt('output.txt',outputar,fmt="%s",delimiter=',')    
print('')
print('clustering result:',M)
'''
np.savetxt('clusteringoutput.txt',C)
'''
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, point_idx))
        