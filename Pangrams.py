#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    # if(s.isalpha() and s.isascii()):
    #     print("pangram")
    # else:
    #     return ("not pangram")
    s=s.lower().replace(" ","")  #convert lowercase+remove space
    letters=set(s)     #to find unique alphabet
    if(set('abcdefghijklmnopqrstuvwxyz').issubset(letters)):  # check all 26 alphabet is contain or not 
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
