#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven",   "eight", "nine", "ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five","twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        return f"{numbers[h]} o' clock"
    elif m == 1:
        return f"one minute past {numbers[h]}"
    elif m == 15:
        return f"quarter past {numbers[h]}"
    elif m == 30:
        return f"half past {numbers[h]}"
    elif m == 45:
        return f"quarter to {numbers[h+1]}"
    elif m < 30:
        return f"{numbers[m]} minutes past {numbers[h]}"
    else:  # m > 30
        return f"{numbers[60 - m]} minutes to {numbers[h+1]}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
