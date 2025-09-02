#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    # result=[]
    # for i in a:
    #     for j in a:
    #         if(i==j):
    #             diff=abs(a.index(j)-a.index(i))
    #             result.append(diff)
    #             maximum=max(diff)
    # return maximum
    result=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]==a[j]):
                diff=abs(j-i)
                result.append(diff)
    if result:
        return min(result)
    else:
        return -1

    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
