#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    # result=s[0]
    # for i in s[1:]:
    #     if(i != result[-1]):
    #         result += i
    # if(result in s):
    #     return "YES"
    # else:
    #     return "NO"
    target="hackerrank"
    j=0
    for i in range(len(s)):
        if(s[i] == target[j]):
            j+=1
        if(j == len(target)):
            return "YES"
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
