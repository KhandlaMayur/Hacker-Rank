#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    color_count={}
    count_num=0
    for i in ar:
        color_count[i]=color_count.get(i,0)+1  #to check if color is allready exit then return current count or not exist then return 0
    for j in color_count.values(): #to take values of piles only not consider piles_color
        count_num +=j//2 
    return count_num
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
