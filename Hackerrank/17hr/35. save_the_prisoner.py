#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    if s + m <= n:
        return (s-1) + m
        
    else:
        remainder = m % n
        mole = s + remainder
        return mole-1
    
    return sum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        # first_multiple_input = input().rstrip().split()

        # n = int(first_multiple_input[0])

        # m = int(first_multiple_input[1])

        # s = int(first_multiple_input[2])

        n = 3
        m = 2
        s = 1

        result = saveThePrisoner(n, m, s)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
