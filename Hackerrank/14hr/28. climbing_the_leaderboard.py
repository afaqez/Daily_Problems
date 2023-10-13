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
    player_rankings = []
    ranked = list(set(ranked))
    ranked = sorted(ranked, reverse=True)
    
    # this is a smart algorithm to solve this problem
    # my solution's logic was accurate but the time complexity was too high because of high iterations
    # this solution doesn't go through everything 
    
    for player_score in player:
        
        while ranked and player_score >= ranked[-1]:
            ranked.pop()
        
        player_rankings.append(len(ranked) + 1)

    return player_rankings
        

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
