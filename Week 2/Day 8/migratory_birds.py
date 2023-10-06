#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    type_count = {}
    max_count = 0
    
    # assigning values 1 or more than 1 to bird types accordingly in a dict
    # if a bird(key) is already in my dict then i will add 1 to its value
    # else we will assign just a 1 
    for bird in arr:
        if bird in type_count:
            type_count[bird] += 1
        else:
            type_count[bird] = 1
            
    max_count = max(type_count.values())
    
    # now lets find the birds with maximum repeatitions
    max_count_birds = [bird for bird, count in type_count.items() if count == max_count]
    
    return min(max_count_birds)
    
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
