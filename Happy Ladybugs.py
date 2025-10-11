#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    counts = Counter(b)
    
    # Check if there is any ladybug with only 1 occurrence
    for k, v in counts.items():
        if k != '_' and v == 1:
            return "NO"
    
    # If there is at least one empty cell, we can rearrange
    if '_' in counts:
        return "YES"
    
    # Otherwise, check if current arrangement is already happy
    for i in range(len(b)):
        if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
            continue
        else:
            return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
