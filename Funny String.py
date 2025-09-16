#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    # m=[]
    # x=[]
    # for i in range(len(s)):
    #     m.append(ord(s[i]))
    # for j in range(len(m)):
    #     diff1=abs(m[j]-m[j+1])
        
    # rev=s[::-1]
    # for k in range(len(rev)):
    #     x.append(ord(rev[k]))
    # for l in range(len(x)):
    #     diff2=abs(x[l]-x[l+1])
    # if(diff1==diff2):
    #     return "Funny"
    # else:
    #     return "Not Funny"
    # rev=s[::-1]
    # for i in range(len(s)):
    #     for j in range(len(rev)):
    #         if(s[i]==rev[j]):
    #             return "Funny"
    #         else:
    #             return "Not Funny"
    
    # x=ord(s)
    # m=ord(rev)
    # if(x[s]==rev[m]):
    #     return "Funny"
    # else:
    #     return "Not Funny"
    rev=s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i-1])):
            return "Not Funny"
    
    return "Funny"

            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
