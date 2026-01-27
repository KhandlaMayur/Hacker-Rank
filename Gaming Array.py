#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    
    # players = ["BOB", "ANDY"]
    # turn = 0  # 0-> BOB 1-> ANDY
    # last_player = None
    
    # while (arr):
    #     player=players[turn]
        
    #     last_player = player
    #     maxi = max(arr)
    #     x=arr.index(maxi)
    #     arr=arr[:x]
    #     turn = 1 - turn
    # return last_player
    biggest = -1
    move_count = 0
    
    for i in arr:
        if(i>biggest):
            biggest = i
            move_count += 1
    
    # if (move_count % 2 == 0):
    #     return "ANDY"
    # else:
    #     return "BOB"
    if (move_count % 2 == 1):
        return "BOB"
    else:
        return "ANDY"
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
