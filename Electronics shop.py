#!/bin/python3

import os
import sys
import random
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #    
     # n=random.choise(keyboards)
    # m=random.choice(drives)
    # total=n+m
    # if(b>total):
    #     return total
    # else:
    #     return -1
    # for n in keyboards:
    #     return keyboards[n]
    # for m in drives:
    #     return drives[m]
    # total=keyboards[n]+drives[m]
    # if (b>total):
    #     return total
    # else:
    #     return -1
    # for n in keyboards:
    #     for m in drives:
    #         if((n+m)<b):
    #             return n+m
    #         else:
    #             return -1
    # cost=-1
    # for n in keyboards:
    #     for m in drives:
    #         if((n+m)<b):
    #             cost=max(cost,(n+m))
    # return cost
    # cost=-1
    # for n in keyboards:
    #     for m in drives:
    #         if((n+m)<=b and (n+m)>b):
    #             cost=n+m
    # return cost
    cost = -1   

    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > cost:
                cost = total

    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
