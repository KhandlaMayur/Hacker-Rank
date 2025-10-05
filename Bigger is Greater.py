#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = list(w)  # convert to list for swapping
    n = len(w)
    
    # Step 1: find pivot
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    
    if i == -1:  # no greater word possible
        return "no answer"
    
    # Step 2: find the smallest char > w[i] from the right
    j = n - 1
    while w[j] <= w[i]:
        j -= 1
    
    # Step 3: swap
    w[i], w[j] = w[j], w[i]
    
    # Step 4: reverse suffix
    w[i+1:] = reversed(w[i+1:])
    
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
