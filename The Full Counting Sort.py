#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    n = len(arr)
    
    for i in range(n // 2):
        arr[i][1] = "-"
    
    buckets = [[] for _ in range(100)]
    
    for num, text in arr:
        num = int(num)
        buckets[num].append(text)
    
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    print(" ".join(result))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
