#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    # for i in range (0,len(unsorted)):
    #     min_inx=i
    #     for j in range(i+1,len(unsorted)):
    #         if(unsorted[min_inx]==unsorted[j]):
    #             return min_inx
    #         if(unsorted[min_inx]>unsorted[j]):
    #             min_inx=j
    #     unsorted[i],unsorted[min_inx]=unsorted[min_inx],unsorted[i]
    # return unsorted
        return sorted(unsorted, key=lambda s: (len(s), s))

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
