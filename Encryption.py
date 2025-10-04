#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    # remove=s.split()
    # lenght_s=len(remove)
    # sqrt=math.sqrt(lenght_s)
    # temp=1
    # while(temp<=sqrt):
    #     temp=sqrt
    #     print(sqrt[0])
    #     temp+=1
    # no_space=s.replace(" ","")
    # lenght_s=len(no_space)
    # sqrt=int(math.sqrt(lenght_s))
    # return no_space[:sqrt]
    # Step 1: remove spaces
    no_space = s.replace(" ", "")
    L = len(no_space)

    # Step 2: find rows and columns
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))

    if (rows * cols < L):
        rows += 1

    # Step 3: build encrypted text column-wise
    result = []
    for c in range(cols):
        word = ""
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                word += no_space[idx]
        result.append(word)

    return " ".join(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
