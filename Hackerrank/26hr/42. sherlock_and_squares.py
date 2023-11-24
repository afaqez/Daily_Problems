#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#


# example: 3 - 9
# take the sqaure root of the upper range which will be equal to 3
# now the '3' means that 3 is there of course BUT the numbers less than 3 which are greater than the lower range are also included
# method to find that was just the square root of lower range and then ceil it to get the exact square
# now diff + 1, 1 is added because of the inclusive range thing


def squares(a, b):
    upper = math.floor(math.sqrt(b))
    lower = math.ceil(math.sqrt(a))
    return (upper - lower) + 1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()



