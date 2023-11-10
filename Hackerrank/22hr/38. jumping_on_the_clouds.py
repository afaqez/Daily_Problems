#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

# i basically iterated with a step of 2 (meaning that I left 2 values on every iteration)
# and checked if the value is 1 or 0 - thunderhead or cumulus cloud
# if the value is 1 then minus 3 otherwise minus 1 from e which is initialized as 100 in the beginning
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    temp = 0
    for i in range(n):
        temp = (temp + k) % n
        if temp == 0:
            if c[temp] == 1:
                e -= 3
            else:
                e -= 1
            return e
            
        if c[temp] == 1:
            e -= 3
        else:
            e -= 1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))
    
    result = jumpingOnClouds(c, k)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
