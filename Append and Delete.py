#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    # if(s==t):
    #     return "Yes"
    # elif(s!=t):
    #     if(s>=t):
    #         len(t) + len(s)
    #         return "No"
    #     elif(s<t):
    #         return "Yes"
    #     else:
    #         return "Yes"
    # else:
    #     return "No"
    # if (s==t):
    #     return "Yes"
    # elif(s!=t):
    #     comman=''.join(set(s) & set(t))
    #     if(s>t):
    #         diff=len(s)-len(comman)
    #         if(diff==k):
    #             return "Yes"
    #         else:
    #             return "No"
    #     else:
    #         if(s<t):
    #             diff=len(t)-len(comman)
    #             if(diff==k):
    #                 return "Yes"
    #             else:
    #                 return "No"
    comman=0
    for i in range(min(len(s),len(t))):
        if (s[i]==t[i]):
            comman+=1
        else:
            break
    mayur=(len(s)-comman ) + (len(t)-comman)   
    if(mayur==k):
        return "Yes"
    elif(mayur < k and (k-mayur)%2==0):
        return "Yes"
    elif(k>len(s)+len(t)):
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
