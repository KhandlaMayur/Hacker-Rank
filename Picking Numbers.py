#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    # max_count=0
    # for i in a:
    #     count=0
    #     for j in a:
    #         if(abs(i-j)<=1):
    #             count+=1
    #     max_count=max(max_count,count)
    # return max_count
        
    # return count
    max_count=0
    for i in a:
        count=0
        for j in a:
            if(i==j or i==j+1):
                count+=1
        max_count=max(max_count,count)
    return max_count
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')

    fptr.close()
