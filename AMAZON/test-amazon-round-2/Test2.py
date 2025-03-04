# A team of financial analysts at Amazon has designed a stock indicator to determine the consistency of Amazon's stock in delivering returns daily. 
# More formally, the percentage return (rounded off to nearest integer) delivered by the stock each day over the last n  days is considered. 
# This is given as an array of integers, stockPrices. The stock's k-consistency score is calculated using the following operations:

# *In a single operation, omit a particular day's return from the stockPrices array to get have one less element, 
# then rejoin the parts of the array. This can be done at most k times *The maximum number of contiguous days during 
# which the daily return was the same is defined as the k-consistency score for Amazon's stock.  Note that the return may be positive or negative.

# As part of the team, you have been assigned to determine the k-consistency score for the stock. 
# You are given an array stockPrices of size n representing the daily percentage return delivered by Amazon stock and a parameter k.

# Determine the k-consistency score.

# Example Consider the percentage return delivered by Amazon's Stock in the last 8 days is represented as 
# stockPrices = [1, -2, 1, 1, 3, 2, 1, -2] and k = 3. https://hrcdn.net/s3_pub/istreet-assets/hXicmMlsj2b2HC3gwvEXiA/Polish_20210904_134057592_resize_53.jpg 
# The optimal approach uses all k operations: *stockPrices = [1, -2, 1, 1, 3 , 2, 1, -2] initially. 
# *Remove stockPrices[4] = 3, the reduced array is stockPrices = [1, -2, 1, 1, 2, 1, -2]. 
# *Remove the integer at index i = 4 in the reduced array, now stockPrices = [1, -2, 1, 1, 1, -2]. 
# *Remove the integer at index i = 1 so stockPrices = [1, 1, 1, 1, -2]. 
# The longest set of contiguous period with the same percentage return is [1, 1, 1, 1].
# The k -consistency score is its length, return 4.

# Complete the function findMaximumScore in the editor below. 
# findMaximumScore has the following parameters:     
# int stockPrices[n]: the percentage return for Amazon stock over the last n days     
# int k: the maximum number of days that can be removed

# Returns     int: the maximum possible k-consistency score

# Sample case STDIN    FUNCTION -----    -------- 6     →  n = 6 1     →  stockPrices = [1, 1, 2, 1, 2, 1] 1 2 1 2 1 3     →  k = 3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMaximumScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockPrices
#  2. INTEGER k
#
def findMaximumScore(stockPrices, k):
    n = len(stockPrices)
    max_score = 0
    
    # Iterate over each unique element in stockPrices
    for unique_value in set(stockPrices):
        left = 0
        removals = 0
        count_same = 0
        
        # Use sliding window technique
        for right in range(n):
            if stockPrices[right] == unique_value:
                count_same += 1
            else:
                removals += 1
            
            # If removals exceed k, move the left pointer to the right
            while removals > k:
                if stockPrices[left] != unique_value:
                    removals -= 1
                else:
                    count_same -= 1
                left += 1
            
            # Update maximum score with the number of same elements in the current window
            max_score = max(max_score, count_same)
    
    return max_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockPrices_count = int(input().strip())

    stockPrices = []

    for _ in range(stockPrices_count):
        stockPrices_item = int(input().strip())
        stockPrices.append(stockPrices_item)

    k = int(input().strip())

    result = findMaximumScore(stockPrices, k)

    fptr.write(str(result) + '\n')

    fptr.close()#!/bin/python3
