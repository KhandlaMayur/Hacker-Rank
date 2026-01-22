#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

# First My Apporach 
# m=[]
# def maximizingXor(l, r):
#     # Write your code here
#     for i in range(l,r+1):
#         for j in range(i,r+1):
#             result= i ^ j
#             m.append(result)
#             maximum=max(m)
#     return maximum

# def maximizingXor(l, r):
#     x=l^r
#     msb=0
#     while(x > 0):
#         msb+=1
#         x >>=1
#     return (1 << msb) -1

def maximizingXor(l, r):
    count=0
    while (l != r):
        l >>= 1
        r >>= 1
        count+=1
    return(1 << count) -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
