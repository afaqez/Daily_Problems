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


    # if the distribution ends before the last prisoner then simply return (starting point - 1) + m
    # lets say there are 3 prisoners and starting pos is 1 and m = 2
    # 1 + 2 = 3 which satisfies my condition and it will return (1 - 1) + 2 = 2
    # if we exceed the limit then we jump to else codition

    if s + m <= n:            
        return (s-1) + m
        
    else:

        # get the remainder with the minus 1 already sorted out and take a mod with n which will give us the actual prisoners value
        # if the mod is 0 this means that the rotations are even distributed 

        remainder = (s + m - 1) % n
        if remainder != 0:
            return remainder
        else:
            return n

    
    return sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
