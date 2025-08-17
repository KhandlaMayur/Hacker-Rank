#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest = lowest = scores[0]
    high_breaks = low_breaks = 0
    
    # Iterate through the scores
    for score in scores[1:]:
        if score > highest:
            highest = score
            high_breaks += 1
        elif score < lowest:
            lowest = score
            low_breaks += 1
    
    return [high_breaks, low_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
