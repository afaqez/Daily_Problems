#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(len(arr)):
        left_diagonal_sum += arr[i][i]  # Elements from the left diagonal
        right_diagonal_sum += arr[i][len(arr) - 1 - i]  # Elements from the right diagonal

    return abs(left_diagonal_sum - right_diagonal_sum)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
