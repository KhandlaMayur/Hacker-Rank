#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
    # final_xor=0
    # for i in range(len(arr)):
    #     xor_val=0
    #     for j in range(i,len(arr)):
    #         xor_val ^= arr[j]
    #         final_xor ^= xor_val
    # return final_xor
    n=len(arr)
    if(n % 2 == 0):
        return 0
    result = 0
    for i in range(0,n,2):
        result ^=arr[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
