#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    #Right for some test case 
    # x=sorted(arr)
    # m=[]
    # for i in range(len(x)):
    #     for j in range(i+1,len(x)):
    #         diff=abs(x[i]-x[j])
    #         m.append(diff)
    #         y=min(m)
    # return y
    arr.sort()
    min_diff = abs(arr[1]-arr[0])
    
    for i in range(1,len(arr)):
        diff = abs(arr[i] - arr[i-1])
        
        if(diff < min_diff):
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
