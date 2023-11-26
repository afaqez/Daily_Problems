#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#


# this didn't seem to be that tough
# i already knew that there was gonna be alot of if conditions
# i could've used elifs too, but the heirarchy that i used is kinda okay too, but yes, my code could've been more clean
# the approach that I used is a top down approach, I first check the year and then the month and then the days
# every metric has its own if and its own else and inside each else, there's an opening for the next metric
# combining everything together, it becomes a nested giant

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    
    if y1 > y2:
        fine = 10000
        return fine
    else:
        if y1 < y2:
            return fine # return 0
        else:
            if m1 == m2:
                if d1 > d2:
                    diff = d1 - d2
                    fine = 15 * diff
                    return fine
                else:
                    return fine # return 0
            else:
                if m1 < m2:
                    return fine # return 0
                else:
                    diff = m1 - m2
                    fine = 500 * diff
                    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
