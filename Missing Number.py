#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    freq = {}

    # Count elements in brr
    for num in brr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Subtract the count of elements found in arr
    for num in arr:
        if num in freq:
            freq[num] -= 1

    # Collect numbers which still have non-zero count
    missing = []
    for num in freq:
        if freq[num] > 0:
            missing.append(num)

    return sorted(missing)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
