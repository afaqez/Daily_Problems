#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max_score = []
    min_score = []
    max_count = 0
    min_count = 0

    max_score.append(scores[0])
    min_score.append(scores[0])

    for i in range(1, len(scores)):  # starting from second index of score
        if scores[i] > max_score[-1]:
            max_score.append(scores[i])
            max_count += 1
            
        elif scores[i] < min_score[-1]: # -1 to check the last element always
            min_score.append(scores[i])
            min_count += 1

    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
