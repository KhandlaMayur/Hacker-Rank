#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the previous same character
        else:
            stack.append(char)
    
    # If stack is empty, return "Empty String"
    return ''.join(stack) if stack else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
