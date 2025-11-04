#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    # result=[]
    # sort_arr=sorted(arr)
    # # pick=random.sample(sort_arr,k)
    # # combination=list(itertools.combinations(sort_arr,k))
    # for i in itertools.combinations(sort_arr,k):
    #     unfainess=max(i)-min(i)
    #     result.append(unfainess)
    # return min(result)
    # above the code time complaxcity is very high that is the reason of code crash not wrong solution but this code is valid for some test cases 
    
    arr.sort()
    min_unfairness=float('inf')
    for i in range(len(arr)-k+1):  #to check how many subarray are posible 
        current_unfairness=arr[i+k-1] -arr[i]  #max-min
        if(current_unfairness < min_unfairness):
            min_unfairness = current_unfairness
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
