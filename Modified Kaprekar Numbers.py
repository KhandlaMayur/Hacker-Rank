#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    result = []
    for n in range(p, q + 1):
        sq = str(n * n)
        d = len(str(n))
        # Right part (last d digits)
        right = int(sq[-d:]) if d <= len(sq) else int(sq)
        # Left part (remaining digits, or 0 if empty)
        left = int(sq[:-d]) if sq[:-d] else 0

        if left + right == n:
            result.append(n)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
