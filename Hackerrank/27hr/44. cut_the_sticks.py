#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


# get the count of the array
# print the count
# get the minimum of the array using min()
# pop the minimum
# subtract minimum from each element
# if any element = 0 pop it out too
# a fun challenge would be to do this with recursion, i might give it a go



# def cutTheSticks(arr):
    
#     if len(arr) == 1:
#         print(len(arr))
#         return

#     else:
#         print(len(arr))
#         length = min(arr)
#         pos = arr.index(length)
#         arr.pop(pos)
#         arr = [n - length for n in arr]
#         arr = [n for n in arr if n != 0]
#         cutTheSticks(arr)



# the recursive one was a good solution but i guess we can't modify hackerrank main function

def cutTheSticks(arr):
    lengths = []
    n = len(arr)
    for _ in range(n):
        if len(arr) == 0:
            break
        elif len(arr) == 1:
            lengths.append(len(arr))
            break
        else:
            lengths.append(len(arr))
            length = min(arr)
            arr.pop(arr.index(length))
            arr = [n - length for n in arr]
            arr = [n for n in arr if n != 0]

    return lengths
  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
