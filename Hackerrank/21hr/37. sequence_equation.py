#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#


# for each x, I will find the 1-based index for that x
# for example, if x = 1, I will find the 1-based index of 1
# and after finding the index, i will again find the 1 based index of the previous 1-based index

def permutationEquation(p):
    x = 1
    n = len(p)
    y = []
    for i, num in enumerate(p):
        x_index = p.index(x)
        x_index += 1 # to adjust the 1-based index

        y_index = p.index(x_index)
        y_index += 1 # to adjust the 1-based index
        y.append(y_index)

        x += 1

    return y
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
