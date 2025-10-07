#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n = len(container)

    # Step 1: Find capacity of each container (row sum)
    container_capacity = []
    for i in range(n):
        total = 0
        for j in range(n):
            total += container[i][j]
        container_capacity.append(total)

    # Step 2: Find total balls of each type (column sum)
    type_count = []
    for j in range(n):
        total = 0
        for i in range(n):
            total += container[i][j]
        type_count.append(total)

    # Step 3: Compare after sorting
    container_capacity.sort()
    type_count.sort()

    if container_capacity == type_count:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
