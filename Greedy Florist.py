#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # m=[]
    # c.sort(reverse=True)
    # for i in range(k):
    #     for j in range(len(c)):
    #         if(i<=k):
    #             x=c*1
    #         else:
    #             x=c*2
    #         b=m.append(x)
    #         result=sum(b)
    # return result 
    c.sort(reverse=True)
    total=0
    for i in range(len(c)):
        x=(i // k)+1
        total += x * c[i]
    return total               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
