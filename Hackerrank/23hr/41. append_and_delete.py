#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


# the for loop first finds the number of different elements
# then this will tell me the number of steps to perform in order to make the array the same as 't'
# count will have the number of different elements and count * 2 will give me the number of operations
# xing by 2 means pop() and append()
# and then the abs difference gives me the additional pop steps required
# lets say if the array s > t then than means, i will have to remove the extra elements in the last 
# for example: HACKERHAPPY && HACKERRANK (i will have to remove the last Y too)
# some test cases are still wrong tho, will work on it again

def appendAndDelete(s, t, k):
    s = list(s)
    t = list(t)
    n = len(s)
    m = len(t)
    count = 0
    o_range = max(n, m)

    diff = abs(n - m)
    step = 0

    for s_element, t_element in zip(s, t):
        if s_element != t_element:
            count += 1

    final_steps = (count * 2) + diff
    
    if final_steps <= k:
        return 'Yes'
    else:
        return 'No'
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
