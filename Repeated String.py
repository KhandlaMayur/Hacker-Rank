#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # a=len(s)
    # if(a==n):
    #     return a
    # elif(a!=n):
    #     return n-a
    # else:
    #     return 0
    a = len(s)              
    temp = s.count('a')        
    if a == n:  
        return temp
    elif a != n:  
        repate = n // a        
        remainder = n % a      
        return (temp * repate) + s[:remainder].count('a')
    else:
        return 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
