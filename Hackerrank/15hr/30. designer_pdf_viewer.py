#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    max = 0   
    count = 0
    for letter in word:
        count += 1
        ascii = ord(letter) - 97
        if h[ascii] > h[max]:
            max = ascii
            
    return h[max] * count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

   

    result = designerPdfViewer(h, word)
   
    fptr.write(str(result) + '\n')

    fptr.close()
