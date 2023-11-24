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



# fixed everything, BUT I AM NOT SATISFIED! 
# i will try to do this again with ABON
# i didn't do the right way which was basically 'exhausting' the k variable 
# like, i HAD to do k number of steps and then check if they were the same or not

def appendAndDelete(s, t, k):
    s = list(s)
    t = list(t)
    n = len(s)
    m = len(t)
    anomaly_pos = 0
    loop_range = max(n, m)

    if s == t: # not optimal
        return 'Yes'
        
    elif m > n: #if string t > string s
        if k > n:
            final_steps = n + m
            if final_steps <= k:
                return 'Yes'
            else:
                return 'No'
        

    for i in range(loop_range): # normal (string s > string t)
        if i == n - 1 or i == m - 1:
            anomaly_pos = i + 1
            break
        elif s[i] != t[i]:
            anomaly_pos = i
            break
    


    pop_step = n - anomaly_pos
    append_step = m - anomaly_pos
    final_steps = pop_step + append_step

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


