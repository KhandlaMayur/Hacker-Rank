#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter   

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    #Write your code here
    # m=[]
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if(arr[i]!=arr[j]):
    #             m.append(arr[i])
    # temp=len(m)
    # return temp
    
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
