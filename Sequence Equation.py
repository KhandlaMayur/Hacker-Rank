#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    # x=1
    # m=[]
    # for i in p:
    #     if(x==i):
    #         m.append(i)
    # return m
    
    # y=[]
    # for j in m:
    #     if(i==j):
    #         y.append(j)
    # return y
    
    # z=[]
    # for k in y:
    #     if(x==k):
    #         z.append(k)
    # return z
    result = []
    n = len(p)
    for x in range(1, n+1):  
        k = p.index(x) + 1 # where is my x(one) if found the x(one) then we can plus one beacuse index start with 0 so we can plus one     
        y = p.index(k) + 1 # where is my k(three) if found the k(three) then we can plus one beacuse index start with  so we can plus one 
        result.append(y) # now add the y element in result empty array
    return result # show output
            
            
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
