#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # lsum=0
    # rsum=0
    # for i in arr:
    #     if(arr[i]==1):
    #         return arr
    #     T=len(arr)//2
    #     left=arr[:T]
    #     right=arr[T:]
    #     lsum+=left
    #     rsum+=right
    # if(lsum==rsum):
    #     return "YES"
    # else:
    #     return "No"
    total_sum=sum(arr)
    left_sum=0
    
    for i in arr:
        right_sum=total_sum-left_sum-i
        if(left_sum==right_sum):
            return "YES"
        left_sum+=i
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
