#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


    
def viralAdvertising(n):
    cumulative = 0
    number_of_people = 5
    
    for i in range(n):
        likes = math.floor(number_of_people/2)
        cumulative += likes
        number_of_people = likes * 3
    
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
