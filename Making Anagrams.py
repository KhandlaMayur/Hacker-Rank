#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    freq1 = {}
    freq2 = {}
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
    deletions = 0
    all_chars = set(freq1.keys()).union(set(freq2.keys()))
    for ch in all_chars:
        deletions += abs(freq1.get(ch, 0) - freq2.get(ch, 0))
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
