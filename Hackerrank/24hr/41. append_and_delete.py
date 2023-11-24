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


# changed my whole logic and converted everything on the basis of 'anomaly position'
# some test cases are still wrong tho

def appendAndDelete(s, t, k):
    s = list(s)
    t = list(t)
    n = len(s)
    m = len(t)
    anomaly_pos = 0
    loop_range = max(n, m)

    for i in range(loop_range):
        if i == n - 1 or i == m - 1:
            anomaly_pos = i + 1
        else:
            anomaly_pos = i

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
