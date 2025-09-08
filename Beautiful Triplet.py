#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    # count=0
    # n=len(arr)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             if(arr[j]-arr[i]==d and arr[k]-arr[j]==d):
    #                 count += 1
    # return count
    arr_set=set(arr)
    count=0
    for n in arr:
        if (((n+d) in arr_set) and ((n+2*d) in arr_set)):
            count += 1
    return count
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
