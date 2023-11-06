#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative = 0.0
    positive = 0.0
    zero = 0.0
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        elif arr[i] == 0:
            zero += 1
            
    total = len(arr)
    
    # Calculate the fractions without rounding yet
    positive_fraction = positive / total
    negative_fraction = negative / total
    zero_fraction = zero / total
    
    # Now round each fraction to 6 decimal places when printing
    print(round(positive_fraction, 6))
    print(round(negative_fraction, 6))
    print(round(zero_fraction, 6))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
