#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # distance=0
    # result=[]
    # for i in range(1,n):
        
    #     distance +=1 
    #     if(distance <=n-1):
    #         value=n-c[i]
    #         result.append(value)
    #     elif(distance>0):
    #         value=c[i]+1
    #         result.append(value)
    #     max_distance=max(result)
    # return max_distance
    c.sort()
    max_distance=c[0]
    max_distance=max(max_distance,(n-1)-c[-1])
    for i in range(1,len(c)):
        gap=(c[i]-c[i-1])//2
        max_distance=max(max_distance,gap)
    return max_distance
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
