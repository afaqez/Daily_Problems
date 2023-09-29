#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour, minute, seconds = s[:-2].split(":")
    am_pm = s[-2:]
    
    if am_pm == "AM":
        if hour == "12":
            military_hour = "00"
        else:
            military_hour = hour
    else: 
        if hour == "12":
            military_hour = "12"
        else:
            military_hour = str(int(hour) + 12)
    
    military_time = military_hour + ":" + minute + ":" + seconds
    return military_time
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
