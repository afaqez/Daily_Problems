#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sea_level = 0
    units = 0
    valley_count = 0
    d_count = 0
    for i in range(len(path)):
        if path[i] == 'D':
            units -= 1
            d_count = 1
            if units == sea_level and d_count > 1:
                valley_count += 1
        
        elif path[i] == 'U':
            units += 1
            if units == sea_level:
                valley_count += 1
            
    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
