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





# by k % n, we are sorting out the k being greater than n. Because if k = 2 and n = 3, we want 2 in our k and if k = 9 and n = 2, we want 1 in k
# a[(q - k) % n] will practice the MAXIMUM POTENTIAL of the MODULO operator. By doing this code, I learned the true functionality of this operator. 
# when q = 0, k = 1 it will result in -1
# then I will take the modulo operator to ACTUALLY get the correct index
# if n = 3 then -1 % 3 = 2
# now the first element of b[] will contain the element that has been rotated 'k' times 


def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n
    b = []
    for q in queries:
        b.append(a[(q - k) % n])

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
