#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    count = {}
    
    for bird_id in arr:
        if bird_id in count:
            count[bird_id] += 1
        else:
            count[bird_id] = 1
    
    # Find the maximum frequency
    max_freq = max(count.values())
    
    # Find all bird ids with that max frequency
    most_common = [bird_id for bird_id in count if count[bird_id] == max_freq]
    
    # Return the smallest bird id among those with the max frequency
    return min(most_common)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
