#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    # count=0
    # for i in c:
    #     if(i==0 and i+1==1 ):
    #         count += 2
    #     elif(i==1 and i+1==0 and i+2==0 ):
    #         count += 2
    #     else:
    #         break
            
    # return count
    count=0
    i=0
    n=len(c)
    
    while (i<n-1):
        if i+2<n and c[i+2]==0:
            i+=2
        else:
            i+=1
        count +=1
    return count
        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
