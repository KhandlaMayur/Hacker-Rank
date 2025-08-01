#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]           # Get AM or PM
    hour = int(s[:2])         # Convert hour string to integer
    rest = s[2:-2]            # Get :mm:ss

    if period == 'AM':
        if hour == 12:
            hour = 0          # 12AM -> 00
    else:  # PM
        if hour != 12:
            hour += 12        # Add 12 if not already 12

    return '{:02d}{}'.format(hour, rest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
