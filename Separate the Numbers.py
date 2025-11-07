#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    for i in range(1, n // 2 + 1):
        first = int(s[:i])
        num = first
        new_s = str(num)
        
        # Build the sequence
        while len(new_s) < n:
            num += 1
            new_s += str(num)
        
        # Check if sequence matches
        if new_s == s:
            print("YES", first)
            return
    print("NO")
            

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
