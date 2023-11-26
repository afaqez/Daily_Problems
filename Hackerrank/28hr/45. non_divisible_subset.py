#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#



# get the occurrences 
# check if its divisible by k 
# if yes then append both the numbers to solutions 
# remove duplicates 


def nonDivisibleSubset(k, s):
    solution = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            sum = s[i] + s[j]
            if sum % k != 0:
                solution.append(s[i])
                solution.append(s[j])
        
    solution = list(set(solution))
    return len(solution)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
