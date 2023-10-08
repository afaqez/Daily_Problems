# 3 test cases failed, looked up the problem and that's because hackerrank decided to give the input size of 200,000 lol, have to use a binary tree may be

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    new_ranks = []
    temp = ranked
    j = 0
    for i in range(len(player)):
        temp.append(player[i])
        temp = sorted(temp, reverse=True)
        temp = list(set(temp))
        temp = sorted(temp, reverse=True)
        
        for j in range(len(temp)):
            if temp[j] == player[i]:
                new_ranks.append(j+1)

        

    return new_ranks
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
