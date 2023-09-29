#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):

    total_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    min_sum = total_sum - max_val
    max_sum = total_sum - min_val

    print(min_sum, max_sum, sep=" ")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
