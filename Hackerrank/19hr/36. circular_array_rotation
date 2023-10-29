#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#




# I don't like this coding style, i will def change it tomorrow and make it less complex

def circularArrayRotation(a, k, queries):
    if len(a) % k == 0 and k != 1:
        b = []
        for i in range(len(queries)):
            b.append(a[queries[i]])
        return b
        
    elif len(a) % k != 0:
        b = []
        diff = len(a) % k
        for i in range(len(queries)):
            if i + diff == len(a):
                b.append(a[0])
            else:
                b.append(a[queries[i + diff]])
            
        return b
        
    elif k == 1:
        b = []
        for i in range(len(queries)):
            if i + 1 == len(a):
                b.append(a[0])
            else:
                b.append(a[queries[i + 1]])
            
        return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
